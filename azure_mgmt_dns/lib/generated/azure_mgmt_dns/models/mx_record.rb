# encoding: utf-8
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.

module Azure::ARM::Dns
  module Models
    #
    # An MX record.
    #
    class MxRecord

      include MsRestAzure

      # @return [Integer] Gets or sets the preference metric for this record.
      attr_accessor :preference

      # @return [String] Gets or sets the domain name of the mail host,
      # without a terminating dot.
      attr_accessor :exchange


      #
      # Mapper for MxRecord class as Ruby Hash.
      # This will be used for serialization/deserialization.
      #
      def self.mapper()
        {
          required: false,
          serialized_name: 'MxRecord',
          type: {
            name: 'Composite',
            class_name: 'MxRecord',
            model_properties: {
              preference: {
                required: false,
                serialized_name: 'preference',
                type: {
                  name: 'Number'
                }
              },
              exchange: {
                required: false,
                serialized_name: 'exchange',
                type: {
                  name: 'String'
                }
              }
            }
          }
        }
      end
    end
  end
end