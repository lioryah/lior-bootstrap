# Structure. RepoLayout

## Project CICD Full Pipeline

```mermaid
flowchart LR
  subgraph PROJECT_PARTS["_layout_/parts.conf.yaml"]
      direction LR
      part-vers["items.vers"]
      part-docs["items.docs"]
  end
  subgraph VERSIONS_PART_MANAGED[vers-managed]
      direction LR

      changelog["docs/changelog.md"]
      version_prefix_txt
  end
  subgraph VERSIONS_PART[conf-set]
      direction LR
      part-vers --> part-ly["task -d version"]
      part-ly --> procs-tasks["procs: ./version/Taskfile.yml"]
      part-ly --> settings["settings:./version/*.txt"]
      part-ly --> source-content["source-content: task gitinfo:some"]
      settings --> apply-version-task-api
      procs-tasks --> apply-version-task-api
      source-content --> apply-version-task-api
  end

  subgraph apply-version-task-api[api-set]
      direction LR
      bump-version --> version_prefix_txt
      gen-changelog --> changelog
  end

  subgraph DOCUMENTAION_PART_MANAGED["docs-targets"]
      direction TB
      __site__["__site__"]
      http_res["http://localhost:8000"]
  end
  subgraph DOCUMENTAION_PART
      direction LR
      part-config["task -t mkdocs.yml"]
      part-config --> part-procs["procs: task -t mkdocs.yml"]
      part-config --> product-path["settings: ./mkdocs.yml"]
      part-config --> part-source["source-content:*.md, docs/*"]

      part-procs --> apply-docs-task-api
      part-source --> apply-docs-task-api
      product-path --> apply-docs-task-api


  end
  subgraph apply-docs-task-api[api-set]
      direction LR
      mkdocs-build-site --> __site__
      mkdocs-serve-site --> http_res
  end
  part-docs --> part-config
```

### links sample

```mermaid
flowchart LR;
    A-->B;
    B-->C;
    C-->D;
    D-->E;
    click A "http://www.github.com" _blank
    click B "http://www.github.com" "Open this in a new tab" _blank
    click C href "http://www.github.com" _blank
    click D href "http://www.github.com" "Open this in a new tab" _blank
```
