document.onreadystatechange = function () {
let umfrage_graph = document.getElementById("umfrage_graph_plotly");
let loading_animation = document.getElementById("spinner_plotly");
    if (document.readyState !== "complete") {

        loading_animation.style.display = "block";

        umfrage_graph.style.display = "none";

    }
    else {
        if(document.readyState === "complete")

        loading_animation.style.display = "none";
        umfrage_graph
    }
}