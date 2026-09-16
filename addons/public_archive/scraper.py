import json
import os

def generate_catalog():
    catalog = {
        "provider": "Public Domain & Open Source Archive",
        "items": [
            {
                "id": "item-01",
                "title": "Big Buck Bunny (Direct Stream)",
                "type": "http_stream",
                "stream_url": "https://download.blender.org/peach/bigbuckbunny_movies/big_buck_bunny_720p_h264.mov",
                "art": "https://upload.wikimedia.org/wikipedia/commons/c/c5/Big_buck_bunny_poster_big.jpg"
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
