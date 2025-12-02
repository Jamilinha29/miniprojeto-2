def producer(buffer, pid: int, timesteps: int):
    
    for step in range(timesteps):
        buffer.produce((pid, step))
