var React = require('react')
var ReactDOM = require('react-dom')

var Results = React.createClass({
    loadResultsFromServer: function () {
        $.ajax({
            url: this.props.url,
            datatype: 'json',
            cache: false,
            success: function (data) {
                this.setState({ data: data });
            }.bind(this),
            error: function (xhr, status, err) {
                console.error(this.props.url, status, err.toString());
            }.bind(this)
        });
    },

    getInitialState: function () {
        return { data: [] };
    },
    componentDidMount: function () {
        this.loadResultsFromServer();
    },

    render: function () {
        if (this.state.data.hits) {
            var commentNodes = [this.state.data.hits].map(function (comment) {
                return comment.total;
            });
        }
        return (
            <div>
                <h1>Hello React!</h1>
                <p>Total results : {commentNodes}</p>
            </div>
        )
    }
})

var Result = React.createClass({
    render: function () {
        return (
            <div class="result">
                <h4 className="resultTitle">{this.props.title}</h4>
                {this.props.children}
            </div>
        );
    }
});

var ResultList = React.createClass({
    render: function () {
        if (this.props.data.hits) {
            var resultTotal = this.props.data.hits.total
            var resultNodes = []
            this.props.data.hits['hits'].forEach(function (hits) {
                resultNode = [hits].map(function (result) {
                    return (
                        <Result title={result._source.title}>
                            {result._source.text}
                        </Result>
                    )
                })
                resultNodes.push(resultNode)
            })
        }
        else {
            var resultNodes = []
        }
        return (
            <div class="resultList">
                <h4> Number of results: {resultTotal}</h4>
                {resultNodes}
            </div>
        );
    }
});

var SearchForm = React.createClass({
    handleSubmit: function (e) {
        e.preventDefault();
        var query = ReactDOM.findDOMNode(this.refs.query).value.trim();
        if (!query) {
            return;
        }
        this.props.onQuerySubmit({ query: query });
        return;
    },
    render: function () {
        return (
            <form className="searchForm" onChange={this.handleSubmit}>
                <input type="text" placeholder="Search query" ref="query" />
                <input type="submit" value="Post" />
            </form>
        );
    }
});

var SearchBox = React.createClass({
    loadResultFromServer: function () {
        $.ajax({
            url: this.props.url,
            dataType: 'json',
            success: function (data) {
                this.setState({ data: data });
            }.bind(this),
            error: function (xhr, status, err) {
                console.error(this.props.url, status, err.toString());
            }.bind(this)
        });
    },
    handleQuerySubmit: function (query) {
        $.ajax({
            url: this.props.url,
            dataType: 'json',
            data: query,
            success: function (data) {
                this.setState({ data: data });
            }.bind(this),
            error: function (xhr, status, err) {
                console.error(this.props.url, status, err.toString());
            }.bind(this)
        });
    },
    getInitialState: function () {
        return { data: [] };
    },
    componentDidMount: function () {
        this.loadResultFromServer();
    },
    render: function () {
        return (
            <div className="searchBox">
                <h1>Search</h1>
                <ResultList data={this.state.data} />
                <SearchForm onQuerySubmit={this.handleQuerySubmit} />
            </div>
        );
    }
});

ReactDOM.render(<SearchBox url='search_data/' />,
    document.getElementById('container'))