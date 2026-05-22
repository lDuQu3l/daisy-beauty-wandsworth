from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import os

def enhance_photo(input_path, output_path, warmth=True):
    """Professional photo enhancement for nail art photography."""
    img = Image.open(input_path)
    
    # 1. Slight crop to focus on nails (center crop, 5% from each side)
    w, h = img.size
    crop_w, crop_h = int(w * 0.05), int(h * 0.08)
    img = img.crop((crop_w, crop_h, w - crop_w, h - crop_h))
    
    # 2. Enhance sharpness (makes details pop)
    sharpener = ImageEnhance.Sharpness(img)
    img = sharpener.enhance(1.3)
    
    # 3. Enhance contrast (makes nails stand out)
    contrast = ImageEnhance.Contrast(img)
    img = contrast.enhance(1.15)
    
    # 4. Enhance color saturation (richer, more vibrant)
    color = ImageEnhance.Color(img)
    img = color.enhance(1.2)
    
    # 5. Brightness - slightly brighter for clean look
    brightness = ImageEnhance.Brightness(img)
    img = brightness.enhance(1.08)
    
    # 6. Warmth filter - subtle warm tone for skin/nails
    if warmth:
        r, g, b = img.split()
        r = r.point(lambda i: min(255, int(i * 1.05)))
        b = b.point(lambda i: max(0, int(i * 0.95)))
        img = Image.merge('RGB', (r, g, b))
    
    # 7. Save with high quality
    img.save(output_path, quality=95, optimize=True)
    print(f"✅ Enhanced: {os.path.basename(input_path)} → {os.path.basename(output_path)}")
    print(f"   Size: {img.size[0]}x{img.size[1]}")

# Process all images
input_dir = "/home/ubuntu/hermes-betty/daisy-beauty-wandsworth/images"
output_dir = input_dir  # Overwrite originals

files = [
    ("nail-white-pearl.jpg", True),
    ("nail-gold-ombre.jpg", True),
    ("nail-blue-glitter.jpg", True),
    ("nail-gold-set.jpg", False),  # less warmth, shows tools better
]

for fname, warmth in files:
    input_path = os.path.join(input_dir, fname)
    if os.path.exists(input_path):
        enhance_photo(input_path, input_path, warmth)
    else:
        print(f"⚠️  Not found: {fname}")
