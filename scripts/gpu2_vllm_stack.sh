#!/usr/bin/env bash
# Manage the VLLM / Mineru inference stack that normally occupies GPU 2 on patricks-mint.
# Usage: gpu2_vllm_stack.sh [stop|start|status]

set -euo pipefail

CONTAINERS=(
    ssq-embedding
    ssq-router
    ssq-reranker
    ssq-mineru
)

cmd="${1:-status}"

stop_stack() {
    echo "Stopping GPU2 inference stack..."
    for c in "${CONTAINERS[@]}"; do
        if docker ps -q -f name="^/${c}$" | grep -q .; then
            echo "  stopping $c"
            docker stop --time 60 "$c" >/dev/null
        else
            echo "  $c already stopped"
        fi
    done
    echo "GPU2 stack stopped."
}

start_stack() {
    echo "Starting GPU2 inference stack..."
    for c in "${CONTAINERS[@]}"; do
        echo "  starting $c"
        docker start "$c" >/dev/null
    done
    echo ""
    echo "Waiting for containers to report healthy (60s max)..."
    for c in "${CONTAINERS[@]}"; do
        for i in {1..30}; do
            status=$(docker inspect --format='{{.State.Health.Status}}' "$c" 2>/dev/null || echo "none")
            if [[ "$status" == "healthy" ]]; then
                echo "  $c: healthy"
                break
            fi
            sleep 2
        done
    done
    echo "GPU2 stack started."
    echo ""
    docker ps --filter "name=ssq-" --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
}

status_stack() {
    echo "GPU2 inference stack status:"
    docker ps --filter "name=ssq-" --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
}

case "$cmd" in
    stop)
        stop_stack
        ;;
    start)
        start_stack
        ;;
    status)
        status_stack
        ;;
    *)
        echo "Unknown command: $cmd"
        echo "Usage: $0 [stop|start|status]"
        exit 1
        ;;
esac
