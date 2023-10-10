import yaml
import os

begin_revision = 'c04c8f975270f73bb64e5295757bf30ef498c20a'
project_name = 'SynthCTTraitBased'

severities = [1,10,100,1000,10000]

store_tags = {"caching-storage":"CachingStoragePolicy","default-storage":"DefaultStoragePolicy","bound-checking-storage":"BoundCheckingStorage","cachable-storage":"CachableStorage", "default-storage":"DefaultStorage", "storage-d":"StorageWithD", "storage-cd":"StorageWithCD", "storage-c":"StorageWithC","null-storage":"NullStorage","storage-c2":"OtherStorageWithC"}
trans_tags = {"default-transformer": "DefaultTransformerPolicy", "smoothing-transformer":"SmoothingTransformerPolicy", "default-algorithm":"DefaultAlgorithm", "direct-solving-algorithm":"DirectSolvingAlgorithm","smoothing-algorithm":"SmoothingAlgorithm", "null-algo":"NullAgorithm", "algo-a":"AlgorithmWithA", "algo-a2":"OtherAlgorithmWithA", "algo-b":"AlgorithmWithB", "algo-ab":"AlgorithmWithAB"}
log_tags = {"dev-null-logger": "DevNullPolicy", "expensive-logger":"ExpensiveLogger", "database-logger": "DataBaseLogger"}

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

            component_name = "-".join(parts[:-2])

            for lookup in [store_tags,trans_tags,log_tags]:
                if component_name in lookup:
                    component_name = lookup[component_name]

            print(component_name)

            info_dict["description"] = f"Introduces an artificial regression of {parts[-1]} into the {parts[-2]} function of the {component_name} of {project_name}."
            info_dict["tags"] = ["compile-time","regression","template",f"{parts[-1]}", "synthetic",component_name,project_name]
            revs_dict = dict()
            revs_dict["revision_range"] = dict()
            revs_dict["revision_range"]["start"] = begin_revision
            info_dict["include_revisions"] = revs_dict

            patch_content = contents.replace("%MS%",str(s))

            with open(f"../{project_name}/{name}.info", "w") as info:
                yaml.dump(info_dict,info)

            with open(f"../{project_name}/{name}.patch", "w") as patch:
                patch.write(patch_content)
