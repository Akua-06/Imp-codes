def get_readable_time(seconds: int) -> str:
    days, remainder = divmod(seconds, 86400) 
    hours, remainder = divmod(remainder, 3600) 
    minutes, seconds = divmod(remainder, 60)

    time_parts = []
    if days > 0:
        time_parts.append(f"{days}d")
    if hours > 0:
        time_parts.append(f"{hours}h")
    if minutes > 0:
        time_parts.append(f"{minutes}m")
    if seconds > 0 or not time_parts:
        time_parts.append(f"{seconds}s")

    return " ".join(time_parts)



uptime = get_readable_time(int(time.total_seconds()))
