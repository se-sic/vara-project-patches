import click
from pathlib import Path
import yaml

@click.command()
@click.option("--project-path", type=click.Path(exists=True))
def create_infos(project_path: Path):
    project_path = Path(project_path)
    for patch_file in project_path.glob("*.patch"):
        info_file = patch_file.with_suffix(".info")

        if info_file.exists():
            continue

        patch_info = get_patch_infos(patch_file)
        patch_info["path"] = patch_file.name

        with open(info_file, "w") as f:
            yaml.dump(patch_info, f)

def get_patch_infos(patch_path: Path):
    print(f"Please enter patch infos for {patch_path.name}:")
    shortname = input(f"shortname ({patch_path.stem.replace('-', '_')}): ")
    if len(shortname) == 0:
        shortname = patch_path.stem.replace("-", "_")
        
    project_name = input(f"project name ({patch_path.parent.stem}): ")
    if len(project_name) == 0:
        project_name = patch_path.parent.stem
    
    
    while not (description := input(f"Enter Description: ")):
        pass

    tags = []
    while tag := input(f"Enter tags (Empty to end): "):
        tags.append(tag)

    args = []
    while arg := input(f"Enter argument name (Empty to end): "):
        args.append(arg)

    return {
        "shortname": shortname,
        "project_name": project_name,
        "description": description,
        "tags": tags,
        "arguments": args,
    }

if __name__ == "__main__":
    create_infos()