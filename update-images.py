#!/usr/bin/python
import subprocess

argoApp = 'argocd/myapp'
set_images_cmd = f"argocd app set {argoApp}"
for svc, img in {"nginx": "nginx:1.21.0"}.items():
  set_images_cmd = f"{set_images_cmd} --plugin-env ARGOCD_ENV_{svc.upper()}_IMAGE='{img}'"

output = subprocess.run(set_images_cmd, shell=True, capture_output=True, check=True)