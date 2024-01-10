Traffic Csv network datasets not filtered by Smart Device's MAC Addresses:

Those dataset were collected exploiting tshark [1](https://tshark.dev/setup/install/), [2](https://www.wireshark.org/docs/man-pages/tshark.html)

#### Example 1a: single extraction
``` bash
time tshark -r capture.pcap -t ud -Y 'ip.addr and tcp.srcport and eth.addr' \
            -T fields -e _ws.col.Time -e eth.src -e ip.src -e eth.dst \
                                      -e ip.dst -e tcp.srcport \
                                      -e _ws.col.Protocol -e frame.len \
            -E separator=, -E occurrence=f 2>/dev/null > traffic1.csv
```

- Data extracted from [capture.pcap](https://drive.google.com/file/d/109EcjpQVPCbFIfBfzWXAXX_OqZMFcr0w/view?usp=drive_link): [traffic1.csv](https://drive.google.com/file/d/1WWLH-Ct5ztXvj93GSL_M4hsbjsJ620kB/view?usp=drive_link)
- Data extracted from [capture1.pcap](https://drive.google.com/file/d/1vAo32qljcKdNptRxwgr27y6Cqaal9z10/view?usp=drive_link): [traffic2.csv](https://drive.google.com/file/d/1K9OPq9CyEHIMRiQGj9oUKHMMzUflBfL1/view?usp=drive_link)
- Data extracted from [capture2.pcap](https://drive.google.com/file/d/1HdUJnZFt64u60xfkJTje5NpT7t_A_j4E/view?usp=drive_link): [traffic3.csv](https://drive.google.com/file/d/1x49E5yhIZew_Q7Nb0E0Hu8lOVN71kSxW/view?usp=drive_link)
- Data extracted from [capture3.pcap](https://drive.google.com/file/d/1K5SUrR9dnTPyd5u9GO6YhMDctYW6jwTc/view?usp=drive_link): [traffic4.csv](https://drive.google.com/file/d/1euEoe-H4iHOhtxf3vR-DJTJFl7QRcdvq/view?usp=drive_link)

#### Example 1b: complete extraction 
``` bash
CAPTURE=( capture.pcap capture1.pcap capture2.pcap capture3.pcap )
TRAFFIC=( traffic1.csv traffic2.csv traffic3.csv traffic4.csv )
for i in {1..4}
do
    time tshark -r "${CAPTURE[i]}" -t ud -Y 'ip.addr and tcp.srcport and eth.addr' \
                -T fields -e _ws.col.Time -e eth.src -e ip.src -e eth.dst \
                                          -e ip.dst -e tcp.srcport \
                                          -e _ws.col.Protocol -e frame.len \
                -E separator=, -E occurrence=f 2>/dev/null > "${TRAFFIC[i]}"
done
```

It's possible to produce a single file using a bash `for` loop statement.
#### Example 2: all in one extraction
``` bash
CAPTURE=( capture.pcap capture1.pcap capture2.pcap capture3.pcap )
truncate -s 0 traffic.csv
for i in {1..4}
do
    time tshark -r "${CAPTURE[i]}" -t ud -Y 'ip.addr and tcp.srcport and eth.addr' \
                -T fields -e _ws.col.Time -e eth.src -e ip.src -e eth.dst \
                                          -e ip.dst -e tcp.srcport \
                                          -e _ws.col.Protocol -e frame.len \
                -E separator=, -E occurrence=f 2>/dev/null >> traffic.csv
done
```
