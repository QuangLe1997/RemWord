
var TopicsListPage = {
	init: function() {
		this.$container = $('.topics-container');
		this.render();
		this.bindEvents();
	},

	render: function() {

	},
};

var VocabularysListPage = {
	init: function() {
		this.$container = $('.vocabularys-container');
		this.render();
		this.bindEvents();
	},

	render: function() {

	},
	};

function myShow() {
  var x = document.getElementById("modal-wrapper");
  x.style.display === "block";
};

$(document).ready(function() {
	TopicsListPage.init();
	VocabularysListPage.init();
});

//document.addEventListener('DOMContentLoaded', function() {
//    var elems = document.querySelectorAll('.fixed-action-btn');
//    var instances = M.FloatingActionButton.init(elems, {
//      direction: 'left'
//    });
//  });



