import Ember from 'ember';

export default Ember.Controller.extend({
  sortedRacesBy: ['num_characters:desc', 'name'],
  sortedRaces: Ember.computed.sort('model', 'sortedRacesBy'),
  chartData: Ember.computed('model', function() {
    return this.get('model').map(function(race) {
      return { value: race.get('num_characters'), label: race.get('name') };
    });
  }),
});
