
import pandas as pd
import requests
import os
import math
from tqdm import tqdm

def get_tile_coords(lat_deg, lon_deg, zoom):
    lat_rad = math.radians(lat_deg)
    n = 2.0 ** zoom
    xtile = int((lon_deg + 180.0) / 360.0 * n)
    ytile = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
    return xtile, ytile

def download_satellite_images(excel_path, output_folder, zoom=18, limit=8000):
    
    df = pd.read_excel(excel_path)
    
    df = df.head(limit)
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    
    base_url = "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}"

    print(f"Downloading {len(df)} images...")
    for index, row in tqdm(df.iterrows(), total=df.shape[0]):
        img_id = int(row['id'])
        lat, lon = row['lat'], row['long']
        
        file_path = os.path.join(output_folder, f"{img_id}.jpg")
        if os.path.exists(file_path): continue

       
        x, y = get_tile_coords(lat, lon, zoom)
        url = base_url.format(z=zoom, y=y, x=x)

        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                with open(file_path, 'wb') as f:
                    f.write(response.content)
        except Exception as e:
            continue

if __name__ == "__main__":
    download_satellite_images("Data/train(1).xlsx", "images/", limit=8000)

if __name__ == "__main__":
    download_satellite_images("Data/test2.xlsx", "images/", limit=5500)