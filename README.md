# 🌍 Network Geo-Mapper

A Python-based project that analyzes captured network traffic to visualize global IP communication paths using geolocation and KML mapping.

## 📌 Project Overview

This project demonstrates how to capture and analyze network traffic using **Wireshark**, extract source and destination IP addresses from a `.pcap` file, determine the host’s public IP location via the `ip-api` API, and geolocate external IPs using the **GeoLiteCity** database with approximately **98% accuracy**. The script then generates a `.kml` file to visualize the communication paths between the host and external IPs in **Google Maps**.

## ⚠️ Privacy Notice

The `.pcap` and `.kml` files used in this project are **not included** in this repository to ensure personal network data and location privacy. These files are listed in `.gitignore`. You are encouraged to test the script using your own clean `.pcap` files or public ones from sources like [Wireshark Sample Captures](https://wiki.wireshark.org/SampleCaptures).

## 🧰 Technologies & Tools

- **Wireshark** – network traffic capture and analysis  
- **Python** – scripting and automation  
  - Libraries: `dpkt`, `pygeoip`, `requests`, `socket`  
- **GeoLiteCity** – offline IP-to-location mapping  
- **Google Earth** – visualization of `.kml` geolocation output  

## 📁 Project Structure
network-geo-mapper/
├── ip_mapper.py     # Main Python script
├── .gitignore       # Excludes private files from repo
└── README.md        # Project documentation


## ▶️ Usage

Place a `.pcap` file named `wire.pcap` in the project folder and make sure `GeoLiteCity.dat` is available. Run the script using Python, and it will generate an `output.kml` file showing the geolocated IP connections, which can be viewed in Google Maps.

