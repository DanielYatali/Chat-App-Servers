const express = require("express");
const socketIo = require("socket.io");
const http = require("http");
const path = require("path");
const PORT = process.env.PORT || 5000;
const app = express();
const server = http.createServer(app);

const io = socketIo(server, {
  cors: {
    origin: [
      "http://localhost:3000",
      ["https://chat-app-phi-ecru.vercel.app/"],
    ],
  },
});

//in case server and client run on different urls

app.use(express.static(path.join(__dirname, "public")));
server.listen(PORT, (err) => {
  if (err) console.log(err);
  console.log("Server running on Port ", PORT);
});

io.on("connection", (socket) => {
  console.log("client connected:", socket.id);
  socket.on("send-message", (msg) => {
    console.log("hi");
    io.emit("receive-message", msg);
  });
  socket.on("disconnect", (reason) => {
    console.log(reason);
  });
});
