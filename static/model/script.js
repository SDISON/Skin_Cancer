(function() {
  var button, parent;

  button = document.querySelector("button");

  parent = button.parentElement;

  button.addEventListener("click", function() {
    parent.classList.add("clicked");
    return setTimeout((function() {
      return parent.classList.add("success");
    }), 2600);
  });

  balapaCop("Upload Progress Interaction", "#999");

}).call(this);

//# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiIiwic291cmNlUm9vdCI6IiIsInNvdXJjZXMiOlsiPGFub255bW91cz4iXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IkFBQUE7QUFBQSxNQUFBLE1BQUEsRUFBQTs7RUFBQSxNQUFBLEdBQVMsUUFBUSxDQUFDLGFBQVQsQ0FBdUIsUUFBdkI7O0VBQ1QsTUFBQSxHQUFTLE1BQU0sQ0FBQzs7RUFFaEIsTUFBTSxDQUFDLGdCQUFQLENBQXdCLE9BQXhCLEVBQWlDLFFBQUEsQ0FBQSxDQUFBO0lBQy9CLE1BQU0sQ0FBQyxTQUFTLENBQUMsR0FBakIsQ0FBcUIsU0FBckI7V0FDQSxVQUFBLENBQVcsQ0FBRSxRQUFBLENBQUEsQ0FBQTthQUFHLE1BQU0sQ0FBQyxTQUFTLENBQUMsR0FBakIsQ0FBcUIsU0FBckI7SUFBSCxDQUFGLENBQVgsRUFBaUQsSUFBakQ7RUFGK0IsQ0FBakM7O0VBSUEsU0FBQSxDQUFVLDZCQUFWLEVBQXlDLE1BQXpDO0FBUEEiLCJzb3VyY2VzQ29udGVudCI6WyJidXR0b24gPSBkb2N1bWVudC5xdWVyeVNlbGVjdG9yIFwiYnV0dG9uXCJcbnBhcmVudCA9IGJ1dHRvbi5wYXJlbnRFbGVtZW50XG5cbmJ1dHRvbi5hZGRFdmVudExpc3RlbmVyIFwiY2xpY2tcIiwgLT5cbiAgcGFyZW50LmNsYXNzTGlzdC5hZGQgXCJjbGlja2VkXCJcbiAgc2V0VGltZW91dCAoIC0+IHBhcmVudC5jbGFzc0xpc3QuYWRkIFwic3VjY2Vzc1wiKSwgMjYwMFxuICBcbmJhbGFwYUNvcCBcIlVwbG9hZCBQcm9ncmVzcyBJbnRlcmFjdGlvblwiLCBcIiM5OTlcIiJdfQ==
//# sourceURL=coffeescript