# Stage 1: Build
FROM gcc:latest AS builder
WORKDIR /app
COPY app.c .
RUN gcc -o app app.c

# Stage 2: Run
FROM debian:stable-slim
WORKDIR /app
COPY --from=builder /app/app .
CMD ["./app"]