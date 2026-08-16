````markdown
# 🌱 Saplings

> Real-time conversations that grow like branches.

Saplings is a real-time communication platform built with **Python, FastAPI, WebSockets, and PostgreSQL**.

The idea is simple: users form interconnected conversations, while real-time events flow through those conversations like pulses through a growing tree.

The project starts from the fundamentals of WebSocket communication and progressively evolves into a production-oriented real-time system.

---

## What We're Building

Saplings will support real-time communication between users through interconnected conversations.

```text
                         Saplings
                            │
              ┌─────────────┼─────────────┐
              │             │             │
           College       Projects       Friends
              │             │             │
           ┌──┴──┐       ┌──┴──┐       ┌──┴──┐
           │     │       │     │       │     │
         Alice  Bob     Alice Charlie Alice David
````

A conversation is more than a collection of messages. It is a live connection between its participants.

---

## Core Features

* Real-time messaging
* Typing indicators
* Online/offline presence
* Group conversations
* Multiple conversations
* Message delivery status
* Read receipts
* Real-time notifications
* Message editing and deletion
* Reconnection
* Offline message synchronization
* Distributed real-time communication
* Horizontal scaling

---

## Tech Stack

| Technology | Purpose                             |
| ---------- | ----------------------------------- |
| Python     | Backend language                    |
| FastAPI    | API & WebSocket server              |
| Uvicorn    | ASGI server                         |
| WebSockets | Real-time communication             |
| asyncio    | Asynchronous I/O                    |
| PostgreSQL | Persistent data                     |
| SQLAlchemy | Database ORM                        |
| Pydantic   | Data validation                     |
| Redis      | Distributed real-time communication |
| Docker     | Containerization                    |

---

## Architecture

### Initial

```text
Client
  │
  ├──────── HTTP ────────► FastAPI
  │
  └────── WebSocket ─────► FastAPI
                             │
                    ┌────────┴────────┐
                    │                 │
               PostgreSQL      Connection Manager
```

### Eventually

```text
                         Clients
                            │
                     Load Balancer
                            │
              ┌─────────────┴─────────────┐
              │                           │
          FastAPI 1                   FastAPI 2
              │                           │
              └─────────────┬─────────────┘
                            │
                       Redis Pub/Sub
                            │
                            ▼
                       PostgreSQL
```

The architecture will evolve as the system encounters real scaling problems.

---

## Roadmap

### 🌱 Foundation

* [ ] WebSocket fundamentals
* [ ] WebSocket handshake
* [ ] Async I/O & event loop
* [ ] First persistent connection
* [ ] Bidirectional communication

### 🌿 Real-Time Communication

* [ ] 1-to-1 messaging
* [ ] Message persistence
* [ ] Connection management
* [ ] Typing indicators
* [ ] Online/offline presence

### 🌳 Conversations

* [ ] Group conversations
* [ ] Multiple conversations / rooms
* [ ] Message history
* [ ] Delivery status
* [ ] Read receipts
* [ ] Real-time notifications
* [ ] Message editing
* [ ] Message deletion

### 🌲 Reliability & Scale

* [ ] Reconnection
* [ ] Offline synchronization
* [ ] Multiple server instances
* [ ] Redis Pub/Sub
* [ ] Cross-server events
* [ ] Horizontal scaling
* [ ] Load balancing

---

## Current Status

**Milestone 0 — Repository initialized**

Next milestone: **WebSocket fundamentals and the first persistent client-server connection.**

```
```
