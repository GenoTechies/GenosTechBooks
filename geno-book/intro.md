# Welcome to your Geno Book

This is a small step taken by Genotechies to allow knowleage generation based on data in Sri Lankan context

<html>
  <head>
    <title>An active web page</title>
    <script type="text/x-thebe-config">
      {
        bootstrap: true,
        selector: "pre",
        requestKernel: true,
    binderOptions: {
        repo: "binder-examples/requirements",
        ref: "master",
    },
      }
    </script>
  <script src="https://unpkg.com/thebe@latest/lib/index.js"></script>
     <script >$.getScript("https://unpkg.com/thebe@latest")
    .done(function (script, textStatus) {
           thebelab.events.on("request-kernel")((kernel) => {
    // Find any cells with an initialization tag and ask Thebe to run them when ready
    kernel.requestExecute({code: "import numpy as np"})
    kernel.requestExecute({code: "import matplotlib.pyplot as plt"})
      });
    })
</script>
  </head>
  <body>
 part 1:
    <pre>
    %matplotlib inline
import ipywidgets as widgets
import requests  # Import the requests library
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
    </pre>
    Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua:
    <pre data-executable="true">
x = np.linspace(0,10)
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
    </pre>
  </body>
</html>
<!-- 
https://github.com/executablebooks/thebe/blob/65800aa141f708476e953c080f12ebbadcf8dd2d/docs/_static/html_examples/demo-status-widget.html -->