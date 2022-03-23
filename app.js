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

//in case server and client run on different urls
const __dirname = path.resolve();
app.use(express.static(join(__dirname, "public")));
// app.get("/", (req, res) => {
//   async function fetchAsync() {
//     let response = await fetch(
//       "https://hpofficepaper-database-chatapp.herokuapp.com/api/users"
//     );
//     let data = await response.json();
//     console.log(data);
//   }

//   fetchAsync();
//   res.send("hello world");
// });
server.listen(PORT, (err) => {
  if (err) console.log(err);
  console.log("Server running on Port ", PORT);
});

io.on("connection", (socket) => {
  console.log("client connected:", socket.id);
  socket.on("join-room", (data) => {
    console.log(data);
    socket.join(data);
  });
  socket.on("send-message", (msg) => {
    async function fetchAsync() {
      let response = await fetch("http://localhost:8080/save/message", {
        method: "POST",
        headers: {
          Accept: "application/json",
          Authorization: "JWT " + msg.token,
          "Content-Type": "application/json",
        },
        body: JSON.stringify(msg),
      });
      let data = await response.json();
      console.log("this");
      console.log(data);
    }

    console.log("hi");
    console.log(msg.conversation_name);
    io.to(msg.conversation_name).emit("receive-message", msg);
    fetchAsync();
  });

  socket.on("disconnect", (reason) => {
    console.log(reason);
  });
});
