import psutil
 
print("=== Monitoring système ===")
 
print(f"CPU : {psutil.cpu_percent()}%")
print(f"RAM : {psutil.virtual_memory().percent}%")
print(f"Disque : {psutil.disk_usage('/').percent}%")
