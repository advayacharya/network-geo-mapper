import dpkt
import socket
import pygeoip
import requests

gi = pygeoip.GeoIP('GeoLiteCity.dat')

# Get your current external location using ip-api
def get_my_location():
    try:
        response = requests.get("http://ip-api.com/json/")
        data = response.json()
        return data["lat"], data["lon"]
    except:
        return None, None

my_lat, my_lon = get_my_location()

def plotIPs(pcap):
    kmlPts = ''
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            KML = retKML(dst, src)
            kmlPts += KML
        except:
            pass
    return kmlPts

def retKML(dstip, srcip):
    dst = gi.record_by_name(dstip)
    try:
        dstlongitude = dst['longitude']
        dstlatitude = dst['latitude']
        if my_lat is None or my_lon is None:
            return ''
        kml = (
            '<Placemark>\n'
            '<name>%s</name>\n'
            '<extrude>1</extrude>\n'
            '<tessellate>1</tessellate>\n'
            '<styleUrl>#transBluePoly</styleUrl>\n'
            '<LineString>\n'
            '<coordinates>%6f,%6f\n%6f,%6f</coordinates>\n'
            '</LineString>\n'
            '</Placemark>\n'
        ) % (dstip, dstlongitude, dstlatitude, my_lon, my_lat)
        return kml
    except:
        return ''

def main():
    with open('wire.pcap', 'rb') as f:
        pcap = dpkt.pcap.Reader(f)
        kmlheader = '<?xml version="1.0" encoding="UTF-8"?>\n<kml xmlns="http://www.opengis.net/kml/2.2">\n<Document>\n'\
                    '<Style id="transBluePoly">\n' \
                    '<LineStyle>\n' \
                    '<width>1.5</width>\n' \
                    '<color>501400E6</color>\n' \
                    '</LineStyle>\n' \
                    '</Style>\n'
        kmlfooter = '</Document>\n</kml>\n'
        kmldoc = kmlheader + plotIPs(pcap) + kmlfooter

    # Write the KML to a file in the same folder
    with open('output.kml', 'w') as kml_file:
        kml_file.write(kmldoc)

if __name__ == '__main__':
    main()
