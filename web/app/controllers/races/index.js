import Ember from 'ember';

export default Ember.Controller.extend({
  splitByClan: false,

  tableData: Ember.computed('model.races', 'model.stats', 'splitByClan', function() {
    if (this.get('splitByClan')) {
      return this.get('model.stats').map((stat) => {
        let race = this.get('model.races').findBy('id', stat.race.toString());
        return {
          id: race.get('id'),
          name: race.get('name') + " - " + race.get('clan_' + stat.clan),
          slug: race.get('slug'),
          num_characters: stat.num_characters,
          race_num_characters: race.get('num_characters'),
          get: function(key) { return this[key]; }
        }
      }).sortBy('race_num_characters').reverse();
    } else {
      return this.get('model.races').sortBy('num_characters').reverse();
    }
  }),
  chartData: Ember.computed('tableData', function() {
    return this.get('tableData').map((race) => {
      return { label: race.get('name'), value: race.get('num_characters') };
    });
  }),
});
