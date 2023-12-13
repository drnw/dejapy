import panel as pn
import param
from elasticsearch_dsl import Document, Double, Text

DEFAULT_MAPPINGS = {
    "Date": param.Date,
    "Double": param.Number,
    "Text": param.String,
    "Keyword": param.String
    # ... Add more as needed
}


def es_to_param_class(es_class) -> param.Parameterized:
    class Base(param.Parameterized):
        def es_upsert(self, document_id=None):
            if document_id:
                # This is an update
                es_instance = es_class.get(id=document_id)
                for field_name, _ in self.param.objects().items():
                    setattr(es_instance, field_name, getattr(self, field_name))
            else:
                # This is a new insert
                es_instance = es_class()
                for field_name, _ in self.param.objects().items():
                    setattr(es_instance, field_name, getattr(self, field_name))
            es_instance.save()

        @classmethod
        def get(cls, document_id):
            es_instance = es_class.get(id=document_id)
            param_instance = cls()
            for field_name, _ in es_instance._d_.items():
                setattr(param_instance, field_name, getattr(es_instance, field_name))
            return param_instance

    fields = es_class._ObjectBase__list_fields()

    # The attribute dict for the new class
    attrs = {}
    for field_name, field_type, _ in fields:
        key = field_type.__class__.__name__
        parameter = DEFAULT_MAPPINGS.get(key)
        if parameter:
            attrs[field_name] = parameter()

    # Now, create a new subclass of Base with the additional parameters
    new_class = type(es_class.__name__, (Base,), attrs)
    return new_class


class Foo(param.Parameterized):
    moniker = param.String(default="P.A. Nelson")
    weight = param.Number(default=82, bounds=(20, 300))


class FooES(Document):
    moniker = Text()
    weight = Double()


FooBar = es_to_param_class(FooES)

pn.extension()


def demo():
    john = Foo()
    john.moniker = "John Doe"
    john.weight = 100

    jane = FooBar()
    jane.moniker = "Jane Doe"
    jane.weight = 60

    return pn.template.BootstrapTemplate(
        title="ES DSL Demo", main=[pn.Param(john), pn.Param(jane)]
    )
