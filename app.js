//Very simple socket server to handle sending messages

import fetch from "node-fetch";
import express from "express";
import { Server } from "socket.io";
import { createServer } from "http";
import { join } from "path";
import path from "path";
const PORT = process.env.PORT || 5000;
const app = express();
const server = createServer(app);

const io = new Server(server, {
  cors: {
    origin: "*",
  },
});

const __dirname = path.resolve();
app.use(express.static(join(__dirname, "public")));

server.listen(PORT, (err) => {
  if (err) console.log(err);
  console.log("Server running on Port ", PORT);
});

io.on("connection", (socket) => {
  console.log("client connected:", socket.id);
  socket.on("join-room", (data) => {
    for (let i = 0; i < data.length; i++) {
      socket.join(data[i]);
    }
  });
  socket.on("send-message", (msg) => {
    //Save message to database
    async function fetchAsync() {
      let response = await fetch(
        "https://myelinking-database-chat-app.herokuapp.com/",
        {
          method: "POST",
          headers: {
            Accept: "application/json",
            Authorization: "JWT " + msg.token,
            "Content-Type": "application/json",
          },
          body: JSON.stringify(msg),
        }
      );
      let data = await response.json();
      console.log(data);
    }

    // console.log(msg.conversation_name);
    //emits msg to conversation
    io.to(msg.conversation_name).emit("receive-message", msg);
    fetchAsync();
  });

  socket.on("disconnect", (reason) => {
    console.log(reason);
  });
});
