#!/usr/bin/env python3
"""Génère des fichiers .wav placeholders pour le timer Blackball."""
import wave
import math
import struct

SR = 44100

def tone(path, freq, duration, fade=0.01):
    n = int(SR * duration)
    frames = []
    for i in range(n):
        t = i / SR
        env = 1.0
        # fondu entrée/sortie
        if i < SR * fade:
            env = i / (SR * fade)
        if i > n - SR * fade:
            env = max(0.0, (n - i) / (SR * fade))
        val = math.sin(2 * math.pi * freq * t) * env
        frames.append(struct.pack('<h', int(val * 32767)))
    with wave.open(path, 'wb') as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(b''.join(frames))
    print("écrit", path)

if __name__ == "__main__":
    import os
    os.makedirs("sounds", exist_ok=True)
    # Avertissement à 25s : bip medium-long
    tone("sounds/25s.wav", freq=1000, duration=0.4)
    # Compte à rebours 5-1 : bip court aigu
    tone("sounds/5s.wav", freq=1200, duration=0.15)
