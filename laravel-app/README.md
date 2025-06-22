## Production Deployment (with Docker)

1. **Set environment variables** in your `.env` file for production (DB, Redis, etc).
2. **Build the Docker image:**
    ```bash
    docker compose build
    ```
3. **Start all services:**
    ```bash
    docker compose up -d
    ```
4. **The app will be available at:**
    - Nginx: [http://localhost:8080](http://localhost:8080)
    - MySQL: port 3306
    - Redis: port 6379

5. **To stop and remove containers, networks, and volumes:**
    ```bash
    docker compose down -v
    ```