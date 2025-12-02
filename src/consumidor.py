def consumer(buffer, cid: int, timesteps: int):
   
    for _ in range(timesteps):
        buffer.consume()
