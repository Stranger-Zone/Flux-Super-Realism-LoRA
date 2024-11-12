from gradio_client import Client

client = Client("prithivMLmods/FLUX-REALISM")
result = client.predict(
		prompt="Hello!!",
		seed=0,
		width=1024,
		height=1024,
		guidance_scale=6,
		randomize_seed=True,
		api_name="/run"
        #takes minimum of 30 seconds
)
print(result)
