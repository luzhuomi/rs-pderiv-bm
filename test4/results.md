
regular expression = $ (a)^{n} (a?)^{n}$
input = $a^n$

| n| re2 | rs-pderiv |
|---|---|---|
|100| 0.003 | 0.014 |
|1000| 0.25 | 0.015 |
|10000| 28 | 0.031|

pyre2

```

$ python3 testre2.py 10000 ~/git/regex-pderiv/benchmarks/bitc/input10000.txt
a
0:00:28.507025
```



```
Ok(
    14.565983ms,
)
./target/release/rs-pderiv 100 ~/git/regex-pderiv/benchmarks/bitc/input100.txt   0.06s  user 0.00s system 79% cpu 0.075 total
avg shared (code):         0 KB
avg unshared (data/stack): 0 KB
total (sum):               0 KB
max memory:                3 MB
page faults from disk:     0
other page faults:         549


Ok(
    15.656243ms,
)
./target/release/rs-pderiv 1000    45.69s  user 0.06s system 99% cpu 45.771 total
avg shared (code):         0 KB
avg unshared (data/stack): 0 KB
total (sum):               0 KB
max memory:                164 MB
page faults from disk:     0
other page faults:         41810


Ok(
    31.396636ms,
)
./target/release/rs-pderiv 10000    44594.02s  user 62.24s system 99% cpu 12:24:20.68 total
avg shared (code):         0 KB
avg unshared (data/stack): 0 KB
total (sum):               0 KB
max memory:                62043 MB
page faults from disk:     7379804
other page faults:         25105965
```



updated


luzm@pop-p52:~/git/rs-pderiv$ /usr/bin/time -v ./target/release/rs-pderiv 10000 ~/git/regex-pderiv/benchmarks/bitc/input10000.txt
[src/main.rs:20] calculate_hash(&r) = 3522703038391445407
[src/main.rs:21] calculate_hash(&calculate_hash(&r)) = 14400948208678772285
[src/regex/pderiv/parse.rs:104] &all_states.len() = 20001
built: 20000
Ok( 
    44090.384919875s,
)
[src/main.rs:27] contents.len() = 10000
mached
Ok( 
    229.015047ms,
)
        Command being timed: "./target/release/rs-pderiv 10000 /home/luzm/git/regex-pderiv/benchmarks/bitc/input10000.txt"
        User time (seconds): 44068.57
        System time (seconds): 24.37
        Percent of CPU this job got: 99%
        Elapsed (wall clock) time (h:mm:ss or m:ss): 12:14:55
        Average shared text size (kbytes): 0
        Average unshared data size (kbytes): 0
        Average stack size (kbytes): 0
        Average total size (kbytes): 0
        Maximum resident set size (kbytes): 71084428
        Average resident set size (kbytes): 0
        Major (requiring I/O) page faults: 0
        Minor (reclaiming a frame) page faults: 17771265
        Voluntary context switches: 1
        Involuntary context switches: 274206
        Swaps: 0
        File system inputs: 0
        File system outputs: 0
        Socket messages sent: 0
        Socket messages received: 0
        Signals delivered: 0
        Page size (bytes): 4096
        Exit status: 0


re2

(test3) luzm@pop-p52:~/git/rs-pderiv-bm/test4$ /usr/bin/time -v python3 testre2.py 10000 ~/git/regex-pderiv/benchmarks/bitc/input10000.txt

0:00:22.481106
        Command being timed: "python3 testre2.py 10000 /home/luzm/git/regex-pderiv/benchmarks/bitc/input10000.txt"
        User time (seconds): 9.61
        System time (seconds): 12.96
        Percent of CPU this job got: 99%
        Elapsed (wall clock) time (h:mm:ss or m:ss): 0:22.58
        Average shared text size (kbytes): 0
        Average unshared data size (kbytes): 0
        Average stack size (kbytes): 0
        Average total size (kbytes): 0
        Maximum resident set size (kbytes): 39088492
        Average resident set size (kbytes): 0
        Major (requiring I/O) page faults: 0
        Minor (reclaiming a frame) page faults: 9789543
        Voluntary context switches: 1
        Involuntary context switches: 376
        Swaps: 0
        File system inputs: 0
        File system outputs: 0
        Socket messages sent: 0
        Socket messages received: 0
        Signals delivered: 0
        Page size (bytes): 4096
        Exit status: 0
