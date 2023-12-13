#	Dejapy
This project is concerned with developing a Panel application which provides similar functionality to [Dejavu from Appbase](https://github.com/appbaseio/dejavu).

`dejavu` is the missing web UI for Elasticsearch and OpenSearch. Existing web UIs leave much to be desired or are built with server-side page rendering techniques that make it less responsive and bulkier to run.

`dejapy` will also provide similar CRUD functionality. However, it will run in Holoviz Panel rather than Node. The project **will not** clone or implement all the feautures of `dejavu`. Rather the goal is to create a lightweight alternative making use of existing Panel copmponents where practical.

# Current status
The project is at prototyping stage. The development approach is exploratory.

The intent is to open source the project. The protoyping will help in presenting the idea to potential sponsors.

# Using Github
The following tabs in Github are important:

- **Code**: The web application with the Python and other files organised to optimise programming, testing and deployment. We avoid putting files into the repo which cannot be easily version controlled e.g. Jupyter Notebooks (.ipynb), Drawio, PDF etc.
- **Wiki**: To capture requirements (either in use cases) or specification by example. To organise the project (stage plans, C4 models, UML, tools etc). To present candidate designs and mock ups.