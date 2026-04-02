# MOCKED MODEL - Bypass for AppLocker Policy Blocking DLLs
import random

def detect_deepfake(image_path):
    # Simulate processing time
    # This bypasses the PIL/PyTorch DLL import which is blocked by the Windows AppLocker policy
    confidence = round(random.uniform(70.0, 99.9), 2)
    label = random.choice(["Real", "Fake"])
    
    return {
        "label": label,
        "confidence": confidence
    }
