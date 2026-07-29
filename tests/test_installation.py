import os, subprocess
from pathlib import Path

def test_local_install_and_status(tmp_path):
    repo=Path(__file__).parents[1]; home=tmp_path/"home"; env={**os.environ,"HOME":str(home),"PRODUCT_HARNESS_REPO_PATH":str(repo)}
    command=[str(repo/"bin/product-harness-install"),"latest"]
    subprocess.run(command,check=True,env=env,text=True,capture_output=True)
    link=home/".agents/skills/product-discovery-harness/product-bootstrap"; assert link.is_symlink()
    link.unlink(); subprocess.run(command,check=True,env=env,text=True,capture_output=True); assert link.is_symlink()
    assert "Repo path:" in subprocess.run([str(repo/"bin/product-harness-status")],check=True,env=env,text=True,capture_output=True).stdout
    cli=home/".agents/skills/product-discovery-harness/product-harness"
    target=tmp_path/"target"
    result=subprocess.run([str(cli),"bootstrap",str(target),"--mode=greenfield"],check=True,env=env,text=True,capture_output=True)
    assert "Validation passed" in result.stdout and (target/"product-harness.yml").exists()
