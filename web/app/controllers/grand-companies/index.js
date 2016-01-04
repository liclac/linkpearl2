import Ember from 'ember';

export default Ember.Controller.extend({
  sortedGCsBy: ['num_characters:desc', 'name'],
  sortedGCs: Ember.computed.sort('model', 'sortedGCsBy'),
  chartData: Ember.computed('model', function() {
    return this.get('model').map(function(gc) {
      return { label: gc.get('name'), value: gc.get('num_characters') };
    });
  }),
});
