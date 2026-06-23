1) В директории `home_works` создать директорию `text_processing`
2) В директории `text_processing` создать файлы
    - `application.log`
    - `metrics`
    - `main.log`
3) Записать 
- в файл `application.log` текст
```text
2024-10-31 04:43:12,591 - DEBUG - User logged in
2024-10-31 04:43:12,591 - INFO - Warning: Low memory
2024-10-31 04:43:12,591 - WARNING - Data retrieved successfully
2024-10-31 04:43:12,591 - DEBUG - Critical error: System failure
2024-10-31 04:43:12,591 - ERROR - Application started
2024-10-31 04:43:12,591 - WARNING - Application started
2024-10-31 04:43:12,591 - DEBUG - Warning: Low memory
2024-10-31 04:43:12,591 - INFO - Application started
2024-10-31 04:43:12,592 - ERROR - Application started
2024-10-31 04:43:12,592 - DEBUG - Application started
2024-10-31 04:43:12,592 - WARNING - Critical error: System failure
2024-10-31 04:43:12,592 - ERROR - Critical error: System failure
2024-10-31 04:43:12,592 - DEBUG - Application shutting down
2024-10-31 04:43:12,592 - DEBUG - Application shutting down
2024-10-31 04:43:12,592 - ERROR - Data retrieved successfully
2024-10-31 04:43:12,592 - INFO - Data retrieved successfully
2024-10-31 04:43:12,592 - ERROR - Warning: Low memory
2024-10-31 04:43:12,592 - WARNING - Error: Failed to connect to the database
2024-10-31 04:43:12,592 - INFO - Critical error: System failure
2024-10-31 04:43:12,592 - DEBUG - Request for data received
2024-10-31 04:43:12,592 - INFO - Critical error: System failure
2024-10-31 04:43:12,592 - INFO - Error: Failed to connect to the database
```
- в файл `metrics` текст
```text
# Application Metrics Log
# metric_name: metric_value
total_requests: 150
successful_requests: 145
failed_requests: 5
average_response_time_ms: 120
max_response_time_ms: 350
min_response_time_ms: 80
memory_usage_mb: 256
cpu_usage_percent: 75
total_requests: 200
successful_requests: 195
failed_requests: 5
average_response_time_ms: 110
memory_usage_mb: 270
cpu_usage_percent: 80
```
- в файл `main.log` текст
```text
2024-10-27 08:15:23 INFO [Server] Application started successfully
2024-10-27 08:17:45 DEBUG [UserService] User login attempt: john_doe@example.com
2024-10-27 08:17:46 INFO [UserService] User john_doe@example.com logged in successfully
2024-10-27 08:20:12 WARN [DatabaseService] High database load detected
2024-10-27 08:22:30 ERROR [PaymentService] Transaction failed for user: alice@example.com
2024-10-27 08:22:31 INFO [PaymentService] Retrying transaction for alice@example.com
2024-10-27 08:22:32 INFO [PaymentService] Transaction successful for alice@example.com
2024-10-27 08:25:00 DEBUG [CacheService] Cache hit ratio: 0.75
2024-10-27 08:35:15 INFO [BackupService] Daily backup started
2024-10-27 08:35:22 ERROR [NetworkService] Connection timeout: 192.168.1.105
2024-10-27 08:35:25 WARN [NetworkService] Retrying connection to 192.168.1.105
2024-10-27 08:35:30 INFO [NetworkService] Connection established with 192.168.1.105
2024-10-27 08:40:00 DEBUG [MemoryManager] Current memory usage: 2.5GB
2024-10-27 08:45:12 INFO [UpdateService] Checking for system updates
2024-10-27 08:45:15 INFO [UpdateService] No new updates available
2024-10-27 08:50:30 WARN [SecurityService] Multiple failed login attempts for user: eve@example.com
2024-10-27 08:50:35 ERROR [SecurityService] Account locked: eve@example.com
2024-10-27 08:55:00 INFO [MonitoringService] All systems operating normally
2024-10-27 09:00:00 INFO [SchedulerService] Running hourly tasks
2024-10-27 09:05:23 DEBUG [APIService] API request received from 10.0.0.15
2024-10-27 09:05:24 ERROR [APIService] Invalid API key from 10.0.0.15
2024-10-27 09:10:00 INFO [LoadBalancer] Traffic distribution: Server1: 40%, Server2: 35%, Server3: 25%
2024-10-27 09:15:30 WARN [DiskService] Low disk space on /dev/sda1: 85% used
2024-10-27 09:20:00 INFO [BackupService] Daily backup completed successfully
2024-10-27 09:25:45 DEBUG [CacheService] Cache invalidation triggered
2024-10-27 09:30:00 INFO [ReportGenerator] Monthly report generation started
```
4) В файле `application.log` 
    - найти все записи ERROR
    - найти все записи WARNING и вывести для них только сообщение
    - найти все записи с Critical в сообщении и посчитать их количество
5) В файле `metrics` 
    - найти метрики, относящиеся к cpu
    - вывести значение метрики `average_response_time_ms`
6) В файле `main.log`
    - найти строки, содержащие ERROR и вывести к какому сервису они относятся
    - найти записи о запросах к APIService
    - вывести все ip-адреса
7) Выполнить команду `free -h` и из ее вывода получить значение столбца available (только для `Mem`, `Swap` НЕ нужен)
