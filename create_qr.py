import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

def create_qr(url, filename, label_color="#d4a0a0"):
    # Create QR code with better error correction for branding
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=12,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    # Style it with rounded modules and brand colors
    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=RoundedModuleDrawer(),
        color_mask=RadialGradiantColorMask(
            back_color=(250, 245, 240),      # cream
            center_color=(212, 160, 160),     # rose
            edge_color=(26, 26, 26),          # charcoal/black
        ),
    )
    
    # Make it bigger
    img = img.resize((1000, 1000), 3)
    
    # Save
    img.save(filename, quality=95)
    print(f"✅ QR created: {filename}")

# QR 1: Website
create_qr(
    "https://lduqu3l.github.io/daisy-beauty-wandsworth/",
    "/home/ubuntu/hermes-betty/daisy-beauty-wandsworth/images/qr-website.png"
)

# QR 2: WhatsApp (placeholder number)
create_qr(
    "https://wa.me/447542496677?text=Hi%20Daisy!%20I%20want%20to%20book%20a%20nail%20appointment%20%F0%9F%92%85",
    "/home/ubuntu/hermes-betty/daisy-beauty-wandsworth/images/qr-whatsapp.png"
)

print("\n🎯 Done! Both QR codes created.")
