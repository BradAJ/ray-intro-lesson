from ray.job_submission import JobSubmissionClient

client = JobSubmissionClient("http://127.0.0.1:8265")

kick_off_mc = (
    # Clone ray. If ray is already present, don't clone again.
    "git clone https://github.com/BradAJ/ray-intro-lesson;"
    # Run the benchmark.
    " python ray-intro-lesson/ray_monte_carlo_script.py"
    " --points 100_000_000 --jobs 10"
)


submission_id = client.submit_job(
    entrypoint=kick_off_mc,
)

print("Use the following command to follow this Job's logs:")
print(f"ray job logs --address='http://localhost:8265' '{submission_id}' --follow")
