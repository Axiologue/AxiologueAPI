// Component for building list of non-Cross Referenced articles
var ArticleList = React.createClass ({displayName: "ArticleList",
  getInitialState: function() {
    return {
      data: [],
    };
  },
  render: function() {
    
    var articleNodes = this.state.data.map(function (article) {
      return (
        React.createElement(ArticleWrapper, {url: article.url, title: article.title, notes: article.notes})
      );
    });

    return ( 
      React.createElement("div", {className: "articleList row"}, 
        React.createElement("h1", null, "Add New article"), 
        React.createElement(ArticleForm, {id: 0, link: "http://localhost:8000/cross/articles/new/"}), 
        React.createElement("h1", null, "Unreferenced Articles"), 
        articleNodes
      )
    );
  },
  componentDidMount: function() {
    $.ajax({
      url: this.props.url,
      dataType: 'json',
      cache: false,
      success: function(data) {
        this.setState({data: data});
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(this.props.url, status, err.toString());
      }.bind(this)
    });
  }
});

// Wrapper class for the individual non-Cross Referenced articles
var ArticleWrapper = React.createClass ({displayName: "ArticleWrapper",
  handleClick: function(key) {
    this.state[key] = !this.state[key];
  },
  getInitialState: function() {
    return {
      cross: false,
      edit: false
    };
  },
  render: function() {

    var buttons = Object.keys(this.state).map(function (key) {
        var classes = "btn btn-block btn-" + key;
        return (
            React.createElement("button", {className: classes, onClick: this.handleClick.bind(this, key)}, 
              key
            )
          )
      },this);
    
    

    return (
      React.createElement("div", {className: "article listitem col-xs-12"}, 
        React.createElement("div", {className: "col-xs-12 col-sm-11"}, 
          React.createElement("ul", null, 
            React.createElement("li", null, React.createElement("strong", null, this.props.title)), 
            React.createElement("li", null, this.props.url), 
            React.createElement("li", null, this.props.notes)
          )
        ), 
        React.createElement("div", {className: "col-sm-1 col-xs-12 text-center"}, 
          buttons
        )
      )
    );
  }
});

// Form for editing and submitting articles
var ArticleForm = React.createClass ({displayName: "ArticleForm",
  render: function() {
    var csrfToken = $.cookie('csrftoken');

    var titleName = 'articleTitle' + this.props.id;
    var urlName = 'articleUrl' + this.props.id;
    var notesName = 'articleNote' + this.props.id;

    return (
        React.createElement("form", {method: "post", action: this.props.link}, 
          React.createElement(DjangoCSRFToken, null), 

          React.createElement("div", {className: "form-group"}, 
            React.createElement("label", {for: titleName}, "Title"), 
            React.createElement("input", {type: "text", name: "title", id: titleName})
          ), 

          React.createElement("div", {className: "form-group"}, 
            React.createElement("label", {for: urlName}, "URL"), 
            React.createElement("input", {type: "text", name: "url", id: urlName})
          ), 

          React.createElement("div", {className: "form-group"}, 
            React.createElement("label", {for: notesName}, "Title"), 
            React.createElement("textarea", {type: "text", name: "title", id: titleName})
          ), 

          React.createElement("button", {type: "submit", className: "btn btn-primary"}, 
            "Submit"
          )

        )
      );
  }
});

// Reusable CSRF token for forms
var DjangoCSRFToken = React.createClass ({displayName: "DjangoCSRFToken",

  render: function() {
    var csrftoken = $.cookie('csrftoken');

    return (
      React.createElement("input", {type: "hidden", name: "csrfmiddlewaretoken", value: csrftoken})
    );
  }
});


// Rendering live elements
React.render(
  React.createElement(ArticleList, {url: "http://localhost:8000/cross/articles/"}),
  document.getElementById('Articles')
);