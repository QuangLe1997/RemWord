
var TopicsListPage = {
	init: function() {
		this.$container = $('.topics-container');
		this.render();
		this.bindEvents();
	},

	render: function() {

	},


//	bindEvents: function() {
//		$('.btn-favorite', this.$container).on('click', function(e) {
//			e.preventDefault();
//
//			var self = $(this);
//			var url = $(this).attr('href');
//			$.getJSON(url, function(result) {
//				if (result.success) {
//					$('.glyphicon-star', self).toggleClass('active');
//				}
//			});
//
//			return false;
//		});
//	}
};

var VocabularysListPage = {
	init: function() {
		this.$container = $('.vocabularys-container');
		this.render();
		this.bindEvents();
	},

	render: function() {

	},

function myShow() {
  var x = document.getElementById("modal-wrapper");
  x.style.display === "block";
};

$(document).ready(function() {
	TopicsListPage.init();
	VocabularysListPage.init();
});



