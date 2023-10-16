# Upsonic Run

The cloud python function runner with docker and Upsonic Cloud.

[Website](https://upsonic.co/upsonic-run) | [Discord](https://discord.gg/) | [Twitter](https://twitter.com/upsonic)




## Installation
You can install Upsonic by pip3:

```console
pip3 install upsonic_run
```



## Implementing
In this point you can use any [Upsonic Cloud](https://docs.upsonic.co/upsonic_cloud.html).


We will use the Free cloud for these examples and for free `YOUR_CLOUD_KEY`:
```console
Upsonic cloud_key
```
>YOUR_CLOUD_KEY = "cloud-***"

Also you can set any string for `YOUR_GLOBAL_ENCRYPTION_KEY` example: 
> YOUR_GLOBAL_ENCRYPTION_KEY = "Thisismypass"

### Basic

```python
from upsonic_run import Upsonic_Run
from upsonic import Upsonic_Cloud

YOUR_CLOUD_KEY = ""
YOUR_GLOBAL_ENCRYPTION_KEY = ""
INTERVAL = 15

cloud = Upsonic_Cloud(YOUR_CLOUD_KEY)
run = Upsonic_Run(cloud, YOUR_GLOBAL_ENCRYPTION_KEY, interval=INTERVAL)


# ------- REGISTER_FUNCTIONS ------- 


@cloud.active(encryption_key=YOUR_GLOBAL_ENCRYPTION_KEY)
def add(a, b, c=5):
    return a + b + c


# ------- RUN ------- 

print(run.run("add", args_for_func=(15, 5), kwargs_for_func={"c": 25}))
```

```console
$ 45
```

### Functions

```
run.add_task("add", endless=False, thread=True, args_for_func=(15, 5), kwargs_for_func={"c": 25})

run.delete_task("add")
```

## Contributing
Contributions to Upsonic Run are welcome! If you have any suggestions or find a bug, please open an issue on the GitHub repository. If you want to contribute code, please fork the repository and create a pull request.

## License
Upsonic Run is released under the MIT License.

<h2 align="center">
    Contributors
</h2>
<p align="center">
    Thank you for your contribution!
</p>
<p align="center">
    <a href="https://github.com/Upsonic/Upsonic-Run/graphs/contributors">
      <img src="https://contrib.rocks/image?repo=Upsonic/Upsonic-Run" />
    </a>
</p>
