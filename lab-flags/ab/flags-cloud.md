# AB tests versus `flupy.org` behind Cloudflare

## 100 requests, concurrency 10

```
$ ab -n 100 -c 10 -e n0100e0010.csv http://flupy.org/data/flags/ar/ar.gif
This is ApacheBench, Version 2.3 <$Revision: 1757674 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking flupy.org (be patient).....done


Server Software:        cloudflare-nginx
Server Hostname:        flupy.org
Server Port:            80

Document Path:          /data/flags/ar/ar.gif
Document Length:        6502 bytes

Concurrency Level:      10
Time taken for tests:   1.267 seconds
Complete requests:      100
Failed requests:        0
Total transferred:      702400 bytes
HTML transferred:       650200 bytes
Requests per second:    78.91 [#/sec] (mean)
Time per request:       126.721 [ms] (mean)
Time per request:       12.672 [ms] (mean, across all concurrent requests)
Transfer rate:          541.30 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        2   62  31.1     77     110
Processing:     4   63  32.4     80     112
Waiting:        4   62  32.1     79     110
Total:          7  126  62.1    146     222

Percentage of the requests served within a certain time (ms)
  50%    146
  66%    167
  75%    168
  80%    169
  90%    172
  95%    181
  98%    217
  99%    222
 100%    222 (longest request)
```

## 1000 requests, concurrency 100

```
$ ab -n 1000 -c 0100 -e n1000e0100.csv http://flupy.org/data/flags/ar/ar.gif
This is ApacheBench, Version 2.3 <$Revision: 1757674 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking flupy.org (be patient)
Completed 100 requests
Completed 200 requests
Completed 300 requests
Completed 400 requests
Completed 500 requests
Completed 600 requests
Completed 700 requests
Completed 800 requests
Completed 900 requests
Completed 1000 requests
Finished 1000 requests


Server Software:        cloudflare-nginx
Server Hostname:        flupy.org
Server Port:            80

Document Path:          /data/flags/ar/ar.gif
Document Length:        6502 bytes

Concurrency Level:      100
Time taken for tests:   1.245 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      7024000 bytes
HTML transferred:       6502000 bytes
Requests per second:    803.17 [#/sec] (mean)
Time per request:       124.507 [ms] (mean)
Time per request:       1.245 [ms] (mean, across all concurrent requests)
Transfer rate:          5509.22 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        4   56 111.9     47    1087
Processing:     7   61  57.3     51     666
Waiting:        6   55  51.7     49     588
Total:         13  117 126.9     98    1208

Percentage of the requests served within a certain time (ms)
  50%     98
  66%    101
  75%    104
  80%    109
  90%    138
  95%    176
  98%    592
  99%   1106
 100%   1208 (longest request)

 ```

 ## 100 requests, concurrency 10, 2nd try

 ```

$ ab -n 100 -c 10 -e n0100e0010t2.csv http://flupy.org/data/flags/ar/ar.gif
This is ApacheBench, Version 2.3 <$Revision: 1757674 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking flupy.org (be patient).....done


Server Software:        cloudflare-nginx
Server Hostname:        flupy.org
Server Port:            80

Document Path:          /data/flags/ar/ar.gif
Document Length:        6502 bytes

Concurrency Level:      10
Time taken for tests:   2.038 seconds
Complete requests:      100
Failed requests:        0
Total transferred:      702400 bytes
HTML transferred:       650200 bytes
Requests per second:    49.08 [#/sec] (mean)
Time per request:       203.754 [ms] (mean)
Time per request:       20.375 [ms] (mean, across all concurrent requests)
Transfer rate:          336.65 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:       28   89  20.0     89     147
Processing:    28  107  85.4     92     696
Waiting:       28   95  39.5     90     388
Total:         66  195  93.9    181     809

Percentage of the requests served within a certain time (ms)
  50%    181
  66%    190
  75%    193
  80%    197
  90%    236
  95%    299
  98%    664
  99%    809
 100%    809 (longest request)

 ```

 ## 9999 requests, concurrency 300

 ```
$ ab -n 9999 -c 300 -e n9999e0300.csv http://flupy.org/data/flags/ar/ar.gif
This is ApacheBench, Version 2.3 <$Revision: 1757674 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking flupy.org (be patient)
socket: Too many open files (24)
```

## 9999 requests, concurrency 200

```
$ ab -n 9999 -c 200 -e n9999e0200.csv http://flupy.org/data/flags/ar/ar.gif
This is ApacheBench, Version 2.3 <$Revision: 1757674 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking flupy.org (be patient)
Completed 999 requests
Completed 1998 requests
Completed 2997 requests
Completed 3996 requests
Completed 4995 requests
Completed 5994 requests
Completed 6993 requests
Completed 7992 requests
Completed 8991 requests
Completed 9990 requests
Finished 9999 requests


Server Software:        cloudflare-nginx
Server Hostname:        flupy.org
Server Port:            80

Document Path:          /data/flags/ar/ar.gif
Document Length:        6502 bytes

Concurrency Level:      200
Time taken for tests:   27.379 seconds
Complete requests:      9999
Failed requests:        1
   (Connect: 0, Receive: 0, Length: 1, Exceptions: 0)
Total transferred:      70227332 bytes
HTML transferred:       65007854 bytes
Requests per second:    365.21 [#/sec] (mean)
Time per request:       547.632 [ms] (mean)
Time per request:       2.738 [ms] (mean, across all concurrent requests)
Transfer rate:          2504.90 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0  104 138.8     88    2678
Processing:     7  144 219.6     91   15096
Waiting:        6  100  61.2     89    1115
Total:         18  248 269.7    176   15096

Percentage of the requests served within a certain time (ms)
  50%    176
  66%    181
  75%    185
  80%    190
  90%    532
  95%    606
  98%   1163
  99%   1222
 100%  15096 (longest request)

```

## 100 requests, concurrency 1

```
 $ ab -n 100 -c 1 -e n0100e0001.csv http://flupy.org/data/flags/ar/ar.gif
 This is ApacheBench, Version 2.3 <$Revision: 1757674 $>
 Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
 Licensed to The Apache Software Foundation, http://www.apache.org/

 Benchmarking flupy.org (be patient).....done


 Server Software:        cloudflare-nginx
 Server Hostname:        flupy.org
 Server Port:            80

 Document Path:          /data/flags/ar/ar.gif
 Document Length:        6502 bytes

 Concurrency Level:      1
 Time taken for tests:   1.221 seconds
 Complete requests:      100
 Failed requests:        0
 Total transferred:      702400 bytes
 HTML transferred:       650200 bytes
 Requests per second:    81.88 [#/sec] (mean)
 Time per request:       12.213 [ms] (mean)
 Time per request:       12.213 [ms] (mean, across all concurrent requests)
 Transfer rate:          561.65 [Kbytes/sec] received

 Connection Times (ms)
               min  mean[+/-sd] median   max
 Connect:        3    4   4.4      3      25
 Processing:     4    8   5.5      6      35
 Waiting:        4    7   5.5      5      34
 Total:          7   12   9.5      9      53

 Percentage of the requests served within a certain time (ms)
   50%      9
   66%     10
   75%     11
   80%     12
   90%     15
   95%     44
   98%     50
   99%     53
  100%     53 (longest request)

```

## 1000 requests, concurrency 1

```

$ ab -n 1000 -c 0001 -e n1000e0001.csv http://flupy.org/data/flags/ar/ar.gif
 This is ApacheBench, Version 2.3 <$Revision: 1757674 $>
 Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
 Licensed to The Apache Software Foundation, http://www.apache.org/

 Benchmarking flupy.org (be patient)
 Completed 100 requests
 Completed 200 requests
 Completed 300 requests
 Completed 400 requests
 Completed 500 requests
 Completed 600 requests
 Completed 700 requests
 Completed 800 requests
 Completed 900 requests
 Completed 1000 requests
 Finished 1000 requests


 Server Software:        cloudflare-nginx
 Server Hostname:        flupy.org
 Server Port:            80

 Document Path:          /data/flags/ar/ar.gif
 Document Length:        6502 bytes

 Concurrency Level:      1
 Time taken for tests:   10.673 seconds
 Complete requests:      1000
 Failed requests:        0
 Total transferred:      7024000 bytes
 HTML transferred:       6502000 bytes
 Requests per second:    93.69 [#/sec] (mean)
 Time per request:       10.673 [ms] (mean)
 Time per request:       10.673 [ms] (mean, across all concurrent requests)
 Transfer rate:          642.66 [Kbytes/sec] received

 Connection Times (ms)
               min  mean[+/-sd] median   max
 Connect:        2    4   2.9      3      27
 Processing:     4    7   4.6      5      83
 Waiting:        4    6   4.6      5      82
 Total:          7   11   6.8      9      86

 Percentage of the requests served within a certain time (ms)
   50%      9
   66%      9
   75%      9
   80%     10
   90%     14
   95%     25
   98%     34
   99%     41
  100%     86 (longest request)
```
