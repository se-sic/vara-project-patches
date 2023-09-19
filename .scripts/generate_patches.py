import yaml
import os

begin_revision = '8c976a890eef105d22defbf28f8a5430abec2131'
tags = ['Synthetic', 'compile-time']
project_name = 'SynthCTCRTP'

severities = [1,10,100,1000,10000]

for template in os.listdir(f"../{project_name}"):
    if not "%MS%" in template:
        continue

    with open(f"../{project_name}/{template}", "r") as f:
        contents = f.read()

        for s in severities:
            stem = template.split(".")[0]

            name = stem.replace("%MS%", str(s)) + "ms"
            
            info_dict = dict()

            info_dict["project_name"] = project_name
            info_dict["shortname"] = name 
            info_dict["path"] = f"{name}.patch"

            parts = name.split('-')

            info_dict["description"] = f"Introduces an artificial regression of {parts[-1]} into {parts[-3]} {parts[-2]}."
            info_dict["tags"] = ["crtp","compile-time","regression","template",f"{parts[-1]}", "synthetic"]
            revs_dict = dict()
            revs_dict["revision_range"] = dict()
            revs_dict["revision_range"]["start"] = begin_revision
            info_dict["include_revisions"] = revs_dict

            patch_content = contents.replace("%MS%",str(s))

            with open(f"../{project_name}/{name}.info", "w") as info:
                yaml.dump(info_dict,info)

            with open(f"../{project_name}/{name}.patch", "w") as patch:
                patch.write(patch_content)


