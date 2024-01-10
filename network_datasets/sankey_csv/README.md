Sankey Csv network datasets filtered by Smart Device's MAC Addresses:
- SMARTBULB TAPO L530E `00:5F:67:BF:09:EF`
- SMARTBULB EZVIZ LB1 `64:F2:FB:DF:FB:E1`
- SMARTPLUG TAPO P100 `E8:48:B8:D6:A8:1D`
- ~~SMARTPLUG EZVIZ T31 `64:F2:FB:48:2C:5B`~~

Those dataset were collected exploiting tshark [1](https://tshark.dev/setup/install/), [2](https://www.wireshark.org/docs/man-pages/tshark.html)

#### Example 1a: single extraction
``` bash
time tshark -r capture.pcap -t ud -Y 'eth.addr==64:f2:fb:df:fb:e1 \
                                   or eth.addr==64:f2:fb:48:2c:5b \
                                   or eth.addr==00:5f:67:bf:09:ef \
                                   or eth.addr==e8:48:b8:d6:a8:1d' \
            -T fields -e _ws.col.Time -e eth.src -e ip.src -e udp.srcport -e tcp.srcport \
                                      -e eth.dst -e ip.dst -e udp.dstport -e tcp.dstport \
                                      -e _ws.col.Protocol -e frame.len \
            -E separator=, -E occurrence=f 2>/dev/null > sankey1.csv
```
- Data extracted from [capture.pcap](https://drive.google.com/file/d/109EcjpQVPCbFIfBfzWXAXX_OqZMFcr0w/view?usp=drive_link): [sankey1.csv](https://drive.google.com/file/d/1TMJvD22uOF0JCRFDdb8T_L4Hg066tjqu/view?usp=drive_link)
- Data extracted from [capture1.pcap](https://drive.google.com/file/d/1vAo32qljcKdNptRxwgr27y6Cqaal9z10/view?usp=drive_link): [sankey2.csv](https://drive.google.com/file/d/14a3g7PICbAsVgpm3Kj3Y_jH4eEOXB32e/view?usp=drive_link)
- Data extracted from [capture2.pcap](https://drive.google.com/file/d/1HdUJnZFt64u60xfkJTje5NpT7t_A_j4E/view?usp=drive_link): [sankey3.csv](https://drive.google.com/file/d/1uYT-YY4nT3NgbPTWxBOsyiDCaVMiZ2AM/view?usp=drive_link)
- Data extracted from [capture3.pcap](https://drive.google.com/file/d/1K5SUrR9dnTPyd5u9GO6YhMDctYW6jwTc/view?usp=drive_link): [sankey4.csv](https://drive.google.com/file/d/1BGzzF0QQ-CBoGEwfj82OPSETSnuL2RKj/view?usp=drive_link)

#### Example 1b: complete extraction 
``` bash
CAPTURE=( capture.pcap capture1.pcap capture2.pcap capture3.pcap )
SANKEY=( sankey1.csv sankey2.csv sankey3.csv sankey4.csv )
for i in {1..4}
do
    time tshark -r "${CAPTURE[i]}" -t ud -Y 'eth.addr==64:f2:fb:df:fb:e1 \
                                          or eth.addr==64:f2:fb:48:2c:5b \
                                          or eth.addr==00:5f:67:bf:09:ef \
                                          or eth.addr==e8:48:b8:d6:a8:1d' \
                -T fields -e _ws.col.Time -e eth.src -e ip.src -e udp.srcport -e tcp.srcport \
                                          -e eth.dst -e ip.dst -e udp.dstport -e tcp.dstport \
                                          -e _ws.col.Protocol -e frame.len \
                -E separator=, -E occurrence=f 2>/dev/null > "${SANKEY[i]}"
done
```

It's possible to produce a single file using a bash `for` loop statement.
#### Example 2: all in one extraction 
``` bash
CAPTURE=( capture.pcap capture1.pcap capture2.pcap capture3.pcap )
truncate -s 0 sankey.csv
for i in {1..4}
do
    time tshark -r "${CAPTURE[i]}" -t ud -Y 'eth.addr==64:f2:fb:df:fb:e1 \
                                          or eth.addr==64:f2:fb:48:2c:5b \
                                          or eth.addr==00:5f:67:bf:09:ef \
                                          or eth.addr==e8:48:b8:d6:a8:1d' \
                -T fields -e _ws.col.Time -e eth.src -e ip.src -e udp.srcport -e tcp.srcport \
                                          -e eth.dst -e ip.dst -e udp.dstport -e tcp.dstport \
                                          -e _ws.col.Protocol -e frame.len \
                -E separator=, -E occurrence=f 2>/dev/null >> sankey.csv
done
```
- [sankey.csv](https://drive.google.com/file/d/1jtMlr4IOpCQIWQ4IPNeUGweSl05Y41dC/view?usp=drive_link)
