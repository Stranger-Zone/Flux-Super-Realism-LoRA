from gradio_client import Client

client = Client("prithivMLmods/FLUX-REALISM")
result = client.predict(
		prompt="A tiny astronaut hatching from an egg on the moon, 4k, planet theme", #your prompt goes here
		seed=0,
		width=1024,
		height=1024,
		guidance_scale=6,
		randomize_seed=True,
		api_name="/run"
        #takes minimum of 30 seconds
)
print(result)
