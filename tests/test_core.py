import ixconfig


TEST_CMDS = {
    'ifconfig': '''
docker0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        inet 172.17.0.1  netmask 255.255.0.0  broadcast 172.17.255.255
        inet6 fe80::42:f2ff:fe23:bb38  prefixlen 64  scopeid 0x20<link>
        ether 02:42:f2:23:bb:38  txqueuelen 0  (Ethernet)
        RX packets 21326  bytes 1178167 (1.1 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 30842  bytes 45098619 (43.0 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

eth0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        ether dc:a6:32:5d:df:cd  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 89  bytes 10104 (9.8 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 89  bytes 10104 (9.8 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

tun0: flags=4305<UP,POINTOPOINT,RUNNING,NOARP,MULTICAST>  mtu 1500
        inet 10.8.0.13  netmask 255.255.255.0  destination 10.8.0.13
        inet6 fe80::5bf:5f0e:ec9e:ba2  prefixlen 64  scopeid 0x20<link>
        unspec 00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00  txqueuelen 100  (UNSPEC)
        RX packets 1499809  bytes 139357734 (132.9 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 2522728  bytes 2760277477 (2.5 GiB)
        TX errors 0  dropped 4463 overruns 0  carrier 0  collisions 0

wlan0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.1.237  netmask 255.255.255.0  broadcast 192.168.1.255
        inet6 2600:6c65:7e80:1518:0:318d:289d:84b6  prefixlen 128  scopeid 0x0<global>
        inet6 2600:6c65:7e80:1518:efe2:110f:ac1d:9641  prefixlen 64  scopeid 0x0<global>
        inet6 fe80::2998:5b3c:8ffb:a03d  prefixlen 64  scopeid 0x20<link>
        ether dc:a6:32:5d:df:ce  txqueuelen 1000  (Ethernet)
        RX packets 1960938  bytes 357377067 (340.8 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 2790429  bytes 3184497906 (2.9 GiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
    ''',
    'ifconfig wlan0': '''
wlan0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.1.237  netmask 255.255.255.0  broadcast 192.168.1.255
        inet6 2600:6c65:7e80:1518:0:318d:289d:84b6  prefixlen 128  scopeid 0x0<global>
        inet6 2600:6c65:7e80:1518:efe2:110f:ac1d:9641  prefixlen 64  scopeid 0x0<global>
        inet6 fe80::2998:5b3c:8ffb:a03d  prefixlen 64  scopeid 0x20<link>
        ether dc:a6:32:5d:df:ce  txqueuelen 1000  (Ethernet)
        RX packets 1960938  bytes 357377067 (340.8 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 2790429  bytes 3184497906 (2.9 GiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
    ''',
    'ifconfig asdfasdfasdf': '''
asdfasdfasdf: error fetching interface information: Device not found
    ''',

    'iwconfig': '''
eth0      no wireless extensions.

wlan0     IEEE 802.11  ESSID:"MySpectrumWiFicc-2G"
          Mode:Managed  Frequency:2.462 GHz  Access Point: A0:8E:78:59:45:D2
          Bit Rate=72.2 Mb/s   Tx-Power=31 dBm
          Retry short limit:7   RTS thr:off   Fragment thr:off
          Power Management:on
          Link Quality=50/70  Signal level=-60 dBm
          Rx invalid nwid:0  Rx invalid crypt:0  Rx invalid frag:0
          Tx excessive retries:32  Invalid misc:0   Missed beacon:0

docker0   no wireless extensions.

lo        no wireless extensions.

tun0      no wireless extensions.
    ''',
    'iwconfig tun0': '''
tun0      no wireless extensions.
    ''',
    'iwconfig adfasdfasdf': '''
adfasdfasdf  No such device
    '''
}

def _get_output(self):
    return TEST_CMDS[self.cmd.strip()]
ixconfig.core._BaseConfig._get_output = _get_output


IFC_RESULT = {
    "docker0": {
        "broadcast": "172.17.255.255",
        "ip": "172.17.0.1",
        "ipv6": "fe80::42:f2ff:fe23:bb38",
        "mac": "02:42:f2:23:bb:38",
        "mtu": 1500,
        "name": "docker0",
        "netmask": "255.255.0.0",
        "rx_dropped": 0,
        "rx_errors": 0,
        "rx_overruns": 0,
        "rx_packets": 21326,
        "tx_carrier": 0,
        "tx_collisions": 0,
        "tx_dropped": 0,
        "tx_errors": 0,
        "tx_overruns": 0,
        "tx_packets": 30842
    },
    "eth0": {
        "mac": "dc:a6:32:5d:df:cd",
        "mtu": 1500,
        "name": "eth0",
        "rx_dropped": 0,
        "rx_errors": 0,
        "rx_overruns": 0,
        "rx_packets": 0,
        "tx_carrier": 0,
        "tx_collisions": 0,
        "tx_dropped": 0,
        "tx_errors": 0,
        "tx_overruns": 0,
        "tx_packets": 0
    },
    "lo": {
        "ip": "127.0.0.1",
        "ipv6": "::1",
        "mtu": 65536,
        "name": "lo",
        "netmask": "255.0.0.0",
        "rx_dropped": 0,
        "rx_errors": 0,
        "rx_overruns": 0,
        "rx_packets": 89,
        "tx_carrier": 0,
        "tx_collisions": 0,
        "tx_dropped": 0,
        "tx_errors": 0,
        "tx_overruns": 0,
        "tx_packets": 89
    },
    "tun0": {
        "ip": "10.8.0.13",
        "ipv6": "fe80::5bf:5f0e:ec9e:ba2",
        "mtu": 1500,
        "name": "tun0",
        "netmask": "255.255.255.0",
        "rx_dropped": 0,
        "rx_errors": 0,
        "rx_overruns": 0,
        "rx_packets": 1499809,
        "tx_carrier": 0,
        "tx_collisions": 0,
        "tx_dropped": 4463,
        "tx_errors": 0,
        "tx_overruns": 0,
        "tx_packets": 2522728
    },
    "wlan0": {
        "broadcast": "192.168.1.255",
        "ip": "192.168.1.237",
        "ipv6": "fe80::2998:5b3c:8ffb:a03d",
        "mac": "dc:a6:32:5d:df:ce",
        "mtu": 1500,
        "name": "wlan0",
        "netmask": "255.255.255.0",
        "rx_dropped": 0,
        "rx_errors": 0,
        "rx_overruns": 0,
        "rx_packets": 1960938,
        "tx_carrier": 0,
        "tx_collisions": 0,
        "tx_dropped": 0,
        "tx_errors": 0,
        "tx_overruns": 0,
        "tx_packets": 2790429
    }
}

IWC_RESULT = {
    "wlan0": {
        "access_point": "A0:8E:78:59:45:D2",
        "bitrate": 72.2,
        "bitrate_unit": "Mb/s",
        "freq": 2.462,
        "freq_unit": "GHz",
        "mode": "Managed",
        "name": "wlan0",
        "power_mgmt": "on",
        "quality": 50.0,
        "quality_ratio": 0.7142857142857143,
        "ssid": "MySpectrumWiFicc-2G",
        "strength": -60.0,
        "strength_unit": "dBm"
    }
}


def test_ifcfg():
    ifc = ixconfig.Ifc()
    print(ifc)
    assert dict(ifc) == IFC_RESULT
    assert ifc.docker0 == IFC_RESULT['docker0']
    assert ifc['docker0'] == IFC_RESULT['docker0']
    assert ifc.get('wlan0') == IFC_RESULT['wlan0']
    assert ifc['wlan0'].ip == IFC_RESULT['wlan0']['ip']
    assert ifc['wlan0']['ip'] == IFC_RESULT['wlan0']['ip']
    assert ifc['wlan0', 'docker0'] == {
        'docker0': IFC_RESULT['docker0'], 'wlan0': IFC_RESULT['wlan0']}

    assert {k for iface, d in ifc.select('ip').items() for k in d} == {'ip'}
    assert set(ifc.ifaces('*0')) == set(IFC_RESULT) - {'lo'}
    assert set(ifc.ifaces('0')) == set(IFC_RESULT) - {'lo'}
    assert ifc.names == list(IFC_RESULT)

    for k in ['wlan0']:
        ifc = ixconfig.Ifc(k)
        print(k, ifc)
        assert dict(ifc) == IFC_RESULT[k]
        assert ifc == IFC_RESULT[k]
        assert ifc.ip == IFC_RESULT[k]['ip']
        assert ifc['ip'] == IFC_RESULT[k]['ip']

    assert ixconfig.Ifc('asdfasdfasdf') == {}

def test_iwcfg():
    iwc = ixconfig.Iwc()
    print(iwc)
    assert dict(iwc) == IWC_RESULT

    iwc = ixconfig.Iwc('tun0')
    print(iwc)
    assert dict(iwc) == {}

    iwc = ixconfig.Iwc('adfasdfasdf')
    print(iwc)
    assert dict(iwc) == {}
