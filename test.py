from flask import Flask, render_template, request
import io
import base64
import numpy as np
from PIL import Image
from ultralytics import YOLO

app = Flask(__name__)

MODEL_PATH = 'best.torchscript'
model = YOLO(MODEL_PATH, task="segment")

@app.route("/", methods=["GET", "POST"])
def predict_img():
    input_image = output_image = None

    if request.method == "POST":
        file = request.files.get('file')
        if not file or file.filename == '':
            return "No file uploaded", 400

        ext = file.filename.rsplit('.', 1)[-1].lower()
        if ext not in ['jpg', 'jpeg', 'png', 'webp']:
            return "Invalid file format. Please upload an image (JPG, JPEG, PNG, WEBP).", 400

        img_bytes = file.read()
        image = Image.open(io.BytesIO(img_bytes)).convert("RGB")
        image_np = np.array(image)

        results = model(image_np)

        detected = any(result.masks is not None and len(result.masks) > 0 for result in results)

        if detected:
            output_image_np = results[0].plot()
            output_image_pil = Image.fromarray(output_image_np)

            buffered = io.BytesIO()
            output_image_pil.save(buffered, format="PNG")
            output_image = base64.b64encode(buffered.getvalue()).decode("utf-8")

            buffered_input = io.BytesIO()
            image.save(buffered_input, format="PNG")
            input_image = base64.b64encode(buffered_input.getvalue()).decode("utf-8")

    return render_template("index.html", input_image=input_image, output_image=output_image)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)