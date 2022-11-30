# Running the Monte Carlo script on an AWS cluster

### Prerequisites:
An Amazon Web Services account with credentials set up to launch and run a EC2 instances from the command line. For more info, see: [Ray on AWS](https://docs.ray.io/en/master/cluster/vms/user-guides/launching-clusters/aws.html).

### Cluster Notes
You can use ray to launch a cluster on a number of different cluster providers/environments. The details that are specific to, for example, AWS are read from a yaml file. In this example see `aws-example-cluster.yaml`, these details are based on the XGBoost Benchmark example in the [Ray Docs](https://docs.ray.io/en/master/cluster/vms/examples/ml-example.html), and which in turn depend on [Ray Jobs SDK](https://docs.ray.io/en/master/cluster/running-applications/job-submission/sdk.html).


### Steps
* Launch cluster on AWS: `ray up -y aws-example-cluster.yaml`
* Wait for the cluster to finish launching.
* IN A SEPARATE TERMINAL, launch local client to monitor cluster. (this will be running continuously while the cluster is up): `ray dashboard aws-example-cluster.yaml`
* Submit your job to the cluster: `python submit_monte_carlo_job.py`
* The job will generate a unique ID of the form `raysubmit_xxxxxxxxxxxxx`, to follow the results run `ray job logs --address='http://localhost:8265' 'raysubmit_xxxxxxxxxxxxx' --follow`. (This command is printed by the python call above)

* **DON'T FORGET TO SHUT DOWN YOUR CLUSTER**: `ray down -y aws-example-cluster.yaml`
