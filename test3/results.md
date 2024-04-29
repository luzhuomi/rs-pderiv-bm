regular expression = $(a?)^{n} (a)^{n}$
input = $a^n$

| n| re2 | rs-pderiv |
|---|---|---|
|100|0.014|0.009|
|1000|24|12.5|
|10000|25337.3|15937.7 |


re2 
```
(test3) luzm@popular:~/git/rs-pderiv-bm/test3$ time python3 testre2.py 100  ~/git/regex-pderiv/benchmarks/bitc/input100.txt
a
0:00:00.007061

(test3) luzm@popular:~/git/rs-pderiv-bm/test3$ time python3 testre2.py 1000  ~/git/regex-pderiv/benchmarks/bitc/input1000.txt
a
0:00:08.633735

real    0m8.660s
user    0m8.582s
sys     0m0.076s


a
7:02:17.335357
python3 testre2.py 10000 ~/git/regex-pderiv/benchmarks/bitc/input10000.txt   25320.52s  user 14.74s system 99% cpu 7:02:17.45 total
avg shared (code):         0 KB
avg unshared (data/stack): 0 KB
total (sum):               0 KB
max memory:                45801 MB
page faults from disk:     0
other page faults:         11741890



rs-pderiv

```
built: 200
Ok(
    575.220491ms,
)
[src/main.rs:27] contents.len() = 100
BitVec<usize, bitvec::order::Lsb0> { addr: 0x55d20ed7f2f0, head: 000000, bits: 100, capacity: 256 } [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
Ok(
    9.020542ms,
)

real    0m0.591s
user    0m0.587s
sys     0m0.004s
luzm@popular:~/git/rs-pderiv$ 




built: 2000
Ok( 
    4919.448030482s,
)
[src/main.rs:27] contents.len() = 1000
BitVec<usize, bitvec::order::Lsb0> { addr: 0x561f23805a10, head: 000000, bits: 1000, capacity: 1024 } [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
Ok( 
    12.525197379s,
)

real    82m12.054s
user    82m10.457s
sys     0m0.861s




ip-172-31-84-125% time ./target/release/rs-pderiv 10000 ~/git/regex-pderiv/benchmarks/bitc/input10000.txt
[src/main.rs:20] calculate_hash(&r) = 11266192224829374616
[src/main.rs:21] calculate_hash(&calculate_hash(&r)) = 6181897037123288864
[src/regex/pderiv/parse.rs:104] &all_states.len() = 20001
built: 20000
Ok(
    164363.444813857s,
)
[src/main.rs:27] contents.len() = 10000
mached
Ok(
    15937.734803669s,
)
./target/release/rs-pderiv 10000    179718.12s  user 576.00s system 99% cpu 50:05:07.97 total
avg shared (code):         0 KB
avg unshared (data/stack): 0 KB
total (sum):               0 KB
max memory:                95435 MB
page faults from disk:     0
other page faults:         317568811





=============

ip-172-31-84-125% time ./target/release/rs-pderiv 100 ~/git/regex-pderiv/benchmarks/bitc/input100.txt
[src/main.rs:20] calculate_hash(&r) = 936750932477591847
[src/main.rs:21] calculate_hash(&calculate_hash(&r)) = 1904562652236551557
[src/regex/pderiv/parse.rs:104] &all_states.len() = 201
built: 200
Ok(
    169.064987ms,
)
[src/main.rs:27] contents.len() = 100
mached
Ok(
    14.510763ms,
)
./target/release/rs-pderiv 100 ~/git/regex-pderiv/benchmarks/bitc/input100.tx   0.18s  user 0.00s system 99% cpu 0.185 total
avg shared (code):         0 KB
avg unshared (data/stack): 0 KB
total (sum):               0 KB
max memory:                4 MB
page faults from disk:     0
other page faults:         708
```



built: 20000
Ok( 
    99627.259391234s,
)
[src/main.rs:27] contents.len() = 10000
mached
Ok( 
    10239.51668394s,
)
        Command being timed: "./target/release/rs-pderiv 10000 /home/luzm/git/regex-pderiv/benchmarks/bitc/input10000.txt"
        User time (seconds): 109480.67
        System time (seconds): 387.92
        Percent of CPU this job got: 99%
        Elapsed (wall clock) time (h:mm:ss or m:ss): 30:31:12
        Average shared text size (kbytes): 0
        Average unshared data size (kbytes): 0
        Average stack size (kbytes): 0
        Average total size (kbytes): 0
        Maximum resident set size (kbytes): 97728368
        Average resident set size (kbytes): 0
        Major (requiring I/O) page faults: 0
        Minor (reclaiming a frame) page faults: 317568923
        Voluntary context switches: 1
        Involuntary context switches: 567598
        Swaps: 0
        File system inputs: 0
        File system outputs: 0
        Socket messages sent: 0
        Socket messages received: 0
        Signals delivered: 0
        Page size (bytes): 4096
        Exit status: 0




re2

(test3) luzm@pop-p52:~/git/rs-pderiv-bm/test3$ /usr/bin/time -v python3 testre2.py 10000 ~/git/regex-pderiv/benchmarks/bitc/input10000.txt
a
6:59:00.095912
        Command being timed: "python3 testre2.py 10000 /home/luzm/git/regex-pderiv/benchmarks/bitc/input10000.txt"
        User time (seconds): 25123.62
        System time (seconds): 14.74
        Percent of CPU this job got: 99%
        Elapsed (wall clock) time (h:mm:ss or m:ss): 6:59:00
        Average shared text size (kbytes): 0
        Average unshared data size (kbytes): 0
        Average stack size (kbytes): 0
        Average total size (kbytes): 0
        Maximum resident set size (kbytes): 46900900
        Average resident set size (kbytes): 0
        Major (requiring I/O) page faults: 0
        Minor (reclaiming a frame) page faults: 11741811
        Voluntary context switches: 1
        Involuntary context switches: 134694
        Swaps: 0
        File system inputs: 0
        File system outputs: 0
        Socket messages sent: 0
        Socket messages received: 0
        Signals delivered: 0
        Page size (bytes): 4096
        Exit status: 0

