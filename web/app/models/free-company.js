import DS from 'ember-data';

export default DS.Model.extend({
  // unsigned 64-bit integer; too big for comfort!
  lodestone_id: DS.attr('string'),
  name: DS.attr('string'),
});
