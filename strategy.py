from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Context:
    def __init__(self, strategy):
        """
        Usually, the Context accepts a strategy through the constructor, but
        also provides a setter to change it at runtime.
        """
        self._strategy = strategy

    @property
    def strategy(self):
        """
        The Context maintains a reference to one of the Strategy objects. The
        Context does not know the concrete class of a strategy. It should work
        with all strategies via the Strategy interface.
        """
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        """
        Usually, the Context allows replacing a Strategy object at runtime.
        """
        self._strategy = strategy

    def do_some_business_logic(self):
        """
        The Context delegates some work to the Strategy object instead of
        implementing multiple versions of the algorithm on its own.
        """

        print("Context: Sorting data using the strategy (not sure how it'll do it)")
        result = self._strategy.do_algorithm(["a", "b", "c", "d", "e"])
        print(",".join(result))


class Strategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """

    @abstractmethod
    def do_algorithm(self, data):
        pass


"""
Concrete Strategies implement the algorithm while following the base Strategy
interface. The interface makes them interchangeable in the Context.
"""


class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data):
        return sorted(data)


class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data):
        return reversed(sorted(data))


if __name__ == "__main__":
    # The client code picks a concrete strategy and passes it to the context.
    # The client should be aware of the differences between strategies in order
    # to make the right choice.

    context = Context(ConcreteStrategyA())
    print("Client: Strategy is set to normal sorting.")
    context.do_some_business_logic()
    print()

    print("Client: Strategy is set to reverse sorting.")
    context.strategy = ConcreteStrategyB()
    context.do_some_business_logic()


class ProStatsPlayerTrendsAPIView(APIView):
    """
    API endpoint to return data used for player trends Highcharts plot.
    """

    http_method_names = ["get"]
    permission_classes = [IsAuthenticatedOrReadOnly]
    renderer_classes = [JSONRenderer]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.current_year = None
        self.metric = None
        self.metric_class_name = None

    def get(self, request, *args, **kwargs):

        # Check if proplayer exists.
        try:
            self.proplayer = ProPlayer.objects.get(id=self.kwargs.get("proplayer_id"))
        except ProPlayer.DoesNotExist:
            raise NotFound(
                detail=f"Pro Stats API - No player found for proplayer_id: {self.kwargs.get('proplayer_id')}"
            )

        # Set instance variables to be used from query_params.
        self._set_instance_variables_from_query_params()

        self.metric_class_name = get_class_name_from_metric_name(self.metric)

        self.metric_class_name.retrieve_data(player_name, start_date, end_date, etc)