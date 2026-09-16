import json
import os
import subprocess

def get_youtube_stream_url(video_url):
    # Try multiple YouTube player clients to bypass restrictions seamlessly
    clients = ["android", "web_embedded", "web"]
    
    for client in clients:
        print(f"Attempting extraction using client: {client}")
        cmd = [
            "yt-dlp", 
            "--extractor-args", f"youtube:player_client={client}", 
            "-g", 
            "-f", "best[ext=mp4]/best", 
            video_url
        ]
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True, timeout=30)
            lines = result.stdout.strip().splitlines()
            if lines:
                print(f"Successfully extracted stream using {client}")
                return lines[0]
        except Exception as e:
            print(f"Client {client} failed: {e}")
            
    raise RuntimeError("All yt-dlp fallback clients failed to extract a stream URL.")

def generate_catalog():
    rickroll_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    print("Extracting fresh YouTube stream link via yt-dlp...")
    direct_stream = get_youtube_stream_url(rickroll_url)
    print(f"Resolved Stream URL: {direct_stream[:60]}...")

    catalog = {
        "provider": "YouTube Test Feed",
        "items": [
            {
                "id": "yt-rickroll",
                "title": "Never Gonna Give You Up (YouTube Live Extract)",
                "type": "http_stream",
                "stream_url": direct_stream,
                "art": "https://i.ytimg.com/vi/dQw4w9WgXcQ/maxresdefault.jpg"
            },
            {
                "id": "item-02",
                "title": "Big Buck Bunny (P2P / Torrent Archive)",
                "type": "p2p_stream",
                "info_hash": "dd825ec313d52361d9f1e1cb07223403dfb3504f",
                "magnet_uri": "magnet:?xt=urn:btih:dd825ec313d52361d9f1e1cb07223403dfb3504f&dn=Big+Buck+Bunny",
                "art": "https://upload.wikimedia.org/wikipedia/commons/c/c5/Big_buck_bunny_poster_big.jpg"
            }
        ]
    }

    output_dir = "addons/public_archive"
    os.makedirs(output_dir, exist_ok=True)
    
    output_path = f"{output_dir}/catalog.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(catalog, f, indent=2)
    
    print(f"Successfully generated catalog at {output_path}")

if __name__ == "__main__":
    generate_catalog()
