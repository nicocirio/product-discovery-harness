import os, subprocess
from pathlib import Path

def test_local_install_and_status(tmp_path):
    """AC-001: installed maintenance commands run from ~/.local/bin."""
    repo=Path(__file__).parents[1]; home=tmp_path/"home"; env={**os.environ,"HOME":str(home),"PRODUCT_HARNESS_REPO_PATH":str(repo),"PRODUCT_HARNESS_LOCAL_CHECKOUT":"1"}
    command=[str(repo/"bin/product-harness-install"),"latest"]
    subprocess.run(command,check=True,env=env,text=True,capture_output=True)
    command_dir = home / ".local/bin"
    assert (command_dir / "product-harness-status").is_symlink()
    command_env = {**env, "PATH": f"{command_dir}:{env['PATH']}"}
    assert "Repo path:" in subprocess.run(["product-harness-status"],check=True,env=command_env,text=True,capture_output=True).stdout
    link=home/".agents/skills/product-discovery-harness/product-bootstrap"; assert link.is_symlink()
    link.unlink(); subprocess.run(command,check=True,env=env,text=True,capture_output=True); assert link.is_symlink()
    assert "Repo path:" in subprocess.run([str(repo/"bin/product-harness-status")],check=True,env=env,text=True,capture_output=True).stdout
    cli=home/".agents/skills/product-discovery-harness/product-harness"
    target=tmp_path/"target"
    result=subprocess.run([str(cli),"bootstrap",str(target),"--mode=greenfield"],check=True,env=env,text=True,capture_output=True)
    assert "Validation passed" in result.stdout and (target/"product-harness.yml").exists()


def test_public_installer_runs_the_refreshed_local_installer(tmp_path):
    """AC-002: an existing checkout receives new command-link behavior on reinstall."""
    repo = Path(__file__).parents[1]
    home = tmp_path / "home"
    env = {**os.environ, "HOME": str(home), "PRODUCT_HARNESS_REPO_PATH": str(repo), "PRODUCT_HARNESS_LOCAL_CHECKOUT": "1"}
    result = subprocess.run([str(repo / "install.sh"), "latest"], check=True, env=env, text=True, capture_output=True)
    assert result.stdout.count("Commands:") == 1
    assert (home / ".local/bin/product-harness-update").is_symlink()
